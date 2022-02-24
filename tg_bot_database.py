from main import loop
from database import Database

import config
import pandas as pd

tg_bot_database = Database(database=config.tg_bot_database, user=config.tg_bot_user,
                           password=config.tg_bot_password, host=config.tg_bot_host,
                           port=config.tg_bot_port, loop=loop)


# ----------------------------------------------------------------------------
#
#
# Функции вызываемые при нажатии /start
#
#
# ----------------------------------------------------------------------------

async def check_if_registered(username):
    """
        Функция для проверки наличия пользователя в базе данных и вывода данных о нем.

        Возвращает:

        username_tg - string
        rights - string
        city - string
        office - string

        """

    query = """SELECT username_tg, rights, city, office FROM tg_bot_database.users WHERE username_tg = $1 ;"""
    async with tg_bot_database.pool.acquire() as connect:
        async with connect.transaction():
            result = await connect.fetchrow(query, username)

    return result


async def user_tg_data_update(username_tg, chat_id, user_id):
    """
        Функция для обновления данных из API Телеграма. А именно chat_id, user_id.

        Возвращает:

        None

        """

    query = """UPDATE tg_bot_database.users SET tg_chat_id = $1, tg_user_id = $2 WHERE username_tg = $3 ;"""
    async with tg_bot_database.pool.acquire() as connect:
        async with connect.transaction():
            await connect.execute(query, chat_id, user_id, username_tg)


# ----------------------------------------------------------------------------
#
#
# Функции вызываемые при работе со списками городов, магазинов, работников или менеджеров
#
#
# ----------------------------------------------------------------------------

async def cities():
    """
        Функция для создания списка городов.

        Возвращает:

        list_of_cities - list

        """

    async with tg_bot_database.pool.acquire() as connect:
        async with connect.transaction():
            query = """SELECT DISTINCT city FROM tg_bot_database.stores ORDER BY city;"""
            cities_from_database = await connect.fetch(query)
        list_of_cities = [row[0] for row in cities_from_database]
        return list_of_cities


async def stores(city):
    """
        Функция для создания списка магазинов в выбранном городе.

        Возвращает:

        list_of_stores - list

        """

    async with tg_bot_database.pool.acquire() as connect:
        async with connect.transaction():
            query = """SELECT store FROM tg_bot_database.stores WHERE city = $1;"""
            stores_from_database = await connect.fetch(query, city)
        list_of_stores = [row[0] for row in stores_from_database]
        return list_of_stores


async def get_list(city, store, rights):
    """
        Функция для создания списка менеджеров или работников в выбранном магазине.

        Возвращает:

        list_of - list

        """

    async with tg_bot_database.pool.acquire() as connect:
        async with connect.transaction():
            query = """SELECT full_name FROM tg_bot_database.users WHERE city = $1 AND office = $2 AND rights 
                        = $3; """
            result = await connect.fetch(query, city, store, rights)
    result_list = [row[0] for row in result]
    return result_list


# ----------------------------------------------------------------------------
#
#
# Функции вызываемые при регистрации номера абонента
#
#
# ----------------------------------------------------------------------------

async def insert_to_customer_number_table(customer_number, date, username_tg):
    """
        Функция для добавления номера абонента и всех данных о том кто добавил в базу данных.
        По умолчанию он не пользователь SuperApp и 'is_seen_in_last_90_days' FALSE.

        Возвращает:

        None

        """

    insert_to_database_query = """INSERT INTO tg_bot_database.customer_numbers (customer_number, office, 
                    date,user_fullname, city) VALUES ($1,$2,$3,$4,$5) ON CONFLICT ON CONSTRAINT unique_number DO NOTHING; """
    select_user_data_from_database = """SELECT full_name, office, city FROM tg_bot_database.users WHERE 
            username_tg = $1; """
    async with tg_bot_database.pool.acquire() as connect:
        async with connect.transaction():
            user_data = await connect.fetchrow(select_user_data_from_database, username_tg)
            await connect.execute(insert_to_database_query, customer_number, user_data['office'], date, user_data['full_name'], user_data['city'])


async def update_90_days_status_customer_number_table(customer_number, message_date, result):
    """
        Функция для обновления статуса 'is_seen_in_last_90_days' абонента.

        Возвращает:

        None

        """

    last_seen_in_super_app = result["last_seen_in_superapp"]
    update_last_seen_90_days_query = """UPDATE tg_bot_database.customer_numbers SET is_seen_in_last_90_days = TRUE WHERE 
                    customer_number = $1; """
    time_delta_90_days = message_date - last_seen_in_super_app
    if time_delta_90_days.days <= 90:
        async with tg_bot_database.pool.acquire() as connect:
            async with connect.transaction():
                await connect.execute(update_last_seen_90_days_query, customer_number)


# ----------------------------------------------------------------------------
#
#
# Функции вызываемые по расписанию каждый день в 8 утра
#
#
# ----------------------------------------------------------------------------

async def scheduled_get_not_superapp_user_customer_number_table():
    """
        Функция для получения списка всех абонентов и дат их регистрации в tg_bot, у кого 'is_superapp_user' = FALSE.

        Возвращает:

        result(customer_number, date) - asyncpg Record

        """

    select_data_query = """SELECT customer_number, date FROM tg_bot_database.customer_numbers WHERE 
        is_superapp_user = FALSE; """
    async with tg_bot_database.pool.acquire() as connect:
        async with connect.transaction():
            result = await connect.fetch(select_data_query)
    return result


async def scheduled_update_users_superapp_status(customer_numbers):
    """
        Функция для обновления статуса 'is_superapp_user' абонента.

        Возвращает:

        Все записи

        """

    update_data_query = """UPDATE tg_bot_database.customer_numbers SET is_superapp_user = TRUE WHERE 
            customer_number = $1 """
    select_query = """SELECT date, city, office, user_fullname, customer_number, is_seen_in_last_90_days, is_superapp_user FROM 
        tg_bot_database.customer_numbers; """
    async with tg_bot_database.pool.acquire() as connect:
        async with connect.transaction():
            for row in customer_numbers:
                await connect.execute(update_data_query, row['customer_number'])
            data = await connect.fetch(select_query)
            list_of_lists = []
            index = 0
            for row in data:
                list_of_lists.append([])
                for item in row:
                    list_of_lists[index].append(item)
                index += 1
    result = pd.DataFrame(list_of_lists)

    return result


# ----------------------------------------------------------------------------
#
#
# Функция вызываемая при работе с правами Manager
#
#
# ----------------------------------------------------------------------------

async def manager_query(operator, employee_name, manager_username, employee_username=None):
    """
        Функция для добавления или удаления работника менеджером.

        Возвращает:

        None.

        """

    async with tg_bot_database.pool.acquire() as connect:
        async with connect.transaction():
            get_manager_data = """SELECT city, office, rights FROM tg_bot_database.users WHERE username_tg = $1"""
            manager_data = await connect.fetchrow(get_manager_data, manager_username)
            if operator == "INSERT":
                query = """INSERT INTO tg_bot_database.users (username_tg, full_name, office, rights, 
                        city) VALUES ($1, $2, $3, $4, $5) ON CONFLICT ON CONSTRAINT unique_user DO NOTHING; """
                await connect.execute(query, employee_username, employee_name, manager_data['office'], 'Worker', manager_data['city'])
            else:
                query = """DELETE FROM tg_bot_database.users WHERE full_name = $1 AND office = $2 AND city = 
                        $3 AND rights = 'Worker'; """
                await connect.execute(query, employee_name, manager_data['office'], manager_data['city'])


# ----------------------------------------------------------------------------
#
#
# Функции вызываемые при работе с правами Admin и Super Admin
#
#
# ----------------------------------------------------------------------------

async def admin_store_query(operator, city, name):
    """
        Функция для добавления или удаления магазина.

        Возвращает:

        None

        """

    async with tg_bot_database.pool.acquire() as connect:
        async with connect.transaction():
            if operator == "INSERT":
                query = """INSERT INTO tg_bot_database.stores (city, store) VALUES ($1, $2) ON CONFLICT ON CONSTRAINT 
                city_store DO NOTHING; """
                await connect.execute(query, city, name)
            else:
                store_query = """DELETE FROM tg_bot_database.stores WHERE store = $1; """  # удаление самого магазин
                await connect.execute(store_query, name)
                users_query = """DELETE FROM tg_bot_database.users WHERE office = $1;"""  # удаление всех работников этого магазина
                await connect.execute(users_query, name)


async def admin_manager_query(operator, city, office, name, username=None):
    """
        Функция для добавления или удаления менеджера выбранного магазина.

        Возвращает:

        result - string. chat_id

        """

    async with tg_bot_database.pool.acquire() as connect:
        async with connect.transaction():
            if operator == "INSERT":
                query = """INSERT INTO tg_bot_database.users (username_tg, full_name, office, rights, city) VALUES (
                $1, $2, $3, $4, $5) ON CONFLICT ON CONSTRAINT unique_user DO UPDATE SET rights = $4 RETURNING 
                tg_chat_id; """
                chat_id = await connect.fetchrow(query, username, name, office, 'Manager', city)
                if chat_id['tg_chat_id'] != 'not set':
                    result = int(chat_id["tg_chat_id"])
                else:
                    result = 'not set'
            else:
                query = """DELETE FROM tg_bot_database.users WHERE full_name = $1 AND office = $2 AND city = $3 
                        AND rights = 'Manager' RETURNING tg_chat_id; """
                chat_id = await connect.fetchrow(query, name, office, city)
                if chat_id['tg_chat_id'] != 'not set':
                    result = int(chat_id["tg_chat_id"])
                else:
                    result = 'not set'

    return result


async def admin_worker_query(operator, city, office, name, username=None):
    """
        Функция для добавления или удаления работника выбранного магазина. Или изменения статуса пользователя с Manager на Worker

        Возвращает:

        result - result - string. chat_id

        """

    async with tg_bot_database.pool.acquire() as connect:
        async with connect.transaction():
            if operator == "INSERT":
                query = """INSERT INTO tg_bot_database.users (username_tg, full_name, office, rights, city) VALUES (
                $1, $2, $3, $4, $5) ON CONFLICT ON CONSTRAINT unique_user DO UPDATE SET rights 
                = 'Worker' RETURNING tg_chat_id; """
                chat_id = await connect.fetchrow(query, username, name, office, 'Worker', city)
                if chat_id['tg_chat_id'] != 'not set':
                    result = int(chat_id["tg_chat_id"])
                else:
                    result = 'not set'
            else:
                query = """DELETE FROM tg_bot_database.users WHERE full_name = $1 AND office = $2 AND city = $3 
                                        AND rights = 'Worker' RETURNING tg_chat_id; """
                chat_id = await connect.fetchrow(query, name, office, city)
                if chat_id['tg_chat_id'] != 'not set':
                    result = int(chat_id["tg_chat_id"])
                else:
                    result = 'not set'

    return result


# ----------------------------------------------------------------------------
#
#
# Функция вызываемая при работе с правами ТОЛЬКО Super Admin
#
#
# ----------------------------------------------------------------------------

async def super_admin_query(operator, username):
    """
        Функция для добавления или удаления пользователей со статусом admin.

        Возвращает:

        result - string. chat_id

        """

    async with tg_bot_database.pool.acquire() as connect:
        async with connect.transaction():
            check_if_exists = """SELECT EXISTS(SELECT * FROM tg_bot_database.users WHERE username_tg = $1);"""
            exists = await connect.fetchrow(check_if_exists, username)
            if exists:
                if operator == "UPDATE":
                    query = """UPDATE tg_bot_database.users SET rights = 'Admin' WHERE username_tg = $1 RETURNING 
                    tg_chat_id; """
                    chat_id = await connect.fetchrow(query, username)
                    if chat_id['tg_chat_id'] != 'not set':
                        result = int(chat_id["tg_chat_id"])
                    else:
                        result = 'not set'
                elif operator == "DELETE":
                    query = """DELETE FROM tg_bot_database.users WHERE username_tg = $1 AND rights = 'Admin' RETURNING 
                    tg_chat_id; """
                    chat_id = await connect.fetchrow(query, username)
                    if chat_id['tg_chat_id'] != 'not set':
                        result = int(chat_id["tg_chat_id"])
                    else:
                        result = 'not set'
    return result


# ----------------------------------------------------------------------------
#
#
# Функция логгирования сообщений от пользователей
#
#
# ----------------------------------------------------------------------------

async def log(username, date, text):
    async with tg_bot_database.pool.acquire() as connect:
        async with connect.transaction():
            query = """INSERT INTO tg_bot_database.messages_from_users (date, username, text) VALUES ($1, $2, 
                    $3); """
            await connect.execute(query, date, username, text)
