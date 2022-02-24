from main import loop
from database import Database

import config
import datetime

eventlog_database = Database(database=config.eventlog_database, user=config.eventlog_user,
                             password=config.eventlog_password, host=config.eventlog_host,
                             port=config.eventlog_port, loop=loop)


async def select_data_from_eventlog_database(customer_number):
    """
    Функция для получения данных об абоненте из базы данных eventlog.

    Возвращает:

    result - asyncpg Record

    """

    select_from_database_query = """SELECT * FROM event_log_database.eventlog WHERE customer_number = $1 ORDER 
    BY last_seen_in_superapp """
    async with eventlog_database.pool.acquire() as connect:
        async with connect.transaction():
            result = await connect.fetchrow(select_from_database_query, customer_number)

    return result


async def scheduled_get_data_from_eventlog(customer_numbers):
    """
        Функция для получения списка абонентов из базы данных eventlog.
        Возвращает номера только тех абонентов, которые были в базе eventlog не больше трех дней с момента регистрации в tg_bot.

        Возвращает:

        result(customer_number) - asyncpg Record

        """

    select_data_query = """SELECT customer_number FROM event_log_database.eventlog WHERE customer_number = $1 AND 
        last_seen_in_superapp >= $2::date AND last_seen_in_superapp <= $3::date  ORDER BY 
        last_seen_in_superapp DESC; """
    async with eventlog_database.pool.acquire() as connect:
        async with connect.transaction():
            result = []
            for row in range(len(customer_numbers)):
                minimum_date = customer_numbers[row]['date']
                maximum_date = customer_numbers[row]['date'] + datetime.timedelta(days=3)
                query_result = await connect.fetch(select_data_query, customer_numbers[row]['customer_number'],
                                                   minimum_date, maximum_date)
                if bool(query_result):
                    result.append(query_result)
    result = [row for record in result for row in record]
    return result


