from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from main import dp, bot
from states import Data_collector_states
import tg_bot_database
import keyboard


@dp.message_handler(Text("Stores"), state=Data_collector_states.admin_waiting)
async def admin_store_options(message: Message):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    user_data = await tg_bot_database.check_if_registered(message.from_user.username)
    if user_data:
        text = """Для <b>добавления</b> магазина нажмите /add_store
Для <b>удаления</b> магазина нажмите /delete_store

<b>Для возврата в основное меню введите</b> /back"""
        await message.answer(text=text, reply_markup=keyboard.admin_stores)
        await Data_collector_states.admin_store.set()


@dp.message_handler(Command("add_store"), state=Data_collector_states.admin_store)
async def add_store(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)

    text = "Выберите <b>город</b>, в который вы хотите <b>добавить</b> магазин. \n \n <b>Для возврата в основное меню " \
           "введите</b> /back "
    list_of_cities = await keyboard.cities_keyboard()
    await message.answer(text=text, reply_markup=list_of_cities)
    await Data_collector_states.admin_add_store_city.set()


@dp.message_handler(Text, state=Data_collector_states.admin_add_store_city)
async def add_store_city(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    city = message.text
    await state.update_data(city=city)
    text = "Введите <b>название</b> магазина. \n \n <b>Для возврата в основное меню введите</b> /back"

    await message.answer(text=text, reply_markup=keyboard.ReplyKeyboardRemove())
    await Data_collector_states.admin_add_store_name.set()


@dp.message_handler(Text, state=Data_collector_states.admin_add_store_name)
async def add_store_name(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    store_name = message.text
    data = await state.get_data()
    store_city = data.get("city")
    await tg_bot_database.admin_store_query("INSERT", store_city, store_name)
    text = """Магазин <b>добавлен</b>.
    
Для <b>работы с магазинами</b> нажмите <b>Stores</b>.
Для <b>работы с менеджерами</b> нажмите <b>Managers</b>.
Для <b>работы с сотрудниками</b> нажмите <b>Workers</b>.
"""
    await message.answer(text=text, reply_markup=keyboard.admin_keyboard)
    await Data_collector_states.admin_waiting.set()


@dp.message_handler(Command("delete_store"), state=Data_collector_states.admin_store)
async def delete_store(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    text = "Выберите <b>город</b>, в котором вы хотите <b>удалить</b> магазин. \n \n <b>Для возврата в основное меню введите</b> /back"
    list_of_cities = await keyboard.cities_keyboard()
    await message.answer(text=text, reply_markup=list_of_cities)
    await Data_collector_states.admin_delete_store_city.set()


@dp.message_handler(Text, state=Data_collector_states.admin_delete_store_city)
async def delete_store_city(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    city = message.text
    await state.update_data(city=city)
    stores = await keyboard.stores_keyboard(city)
    text = "Выберите <b>название</b> магазина, который вы хотите <b>удалить</b>. \n \n <b>Для возврата в основное меню введите</b> /back"

    await message.answer(text=text, reply_markup=stores)
    await Data_collector_states.admin_delete_store_name.set()


@dp.message_handler(Text, state=Data_collector_states.admin_delete_store_name)
async def delete_store_name(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    store_name = message.text
    data = await state.get_data()
    store_city = data.get("city")
    await tg_bot_database.admin_store_query("DELETE", store_city, store_name)
    text = """Магазин <b>удален</b>.

Для <b>работы с магазинами</b> нажмите <b>Stores</b>.
Для <b>работы с менеджерами</b> нажмите <b>Managers</b>.
Для <b>работы с сотрудниками</b> нажмите <b>Workers</b>.
"""
    await message.answer(text=text, reply_markup=keyboard.admin_keyboard)
    await Data_collector_states.admin_waiting.set()


@dp.message_handler(Text("Managers"), state=Data_collector_states.admin_waiting)
async def admin_manager_options(message: Message):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    user_data = await tg_bot_database.check_if_registered(message.from_user.username)
    if user_data:
        text = """Для <b>добавления</b> менеджера нажмите /add_manager
Для <b>удаления</b> менеджера нажмите /delete_manager

<b>Для возврата в основное меню введите</b> /back"""
        await message.answer(text=text, reply_markup=keyboard.admin_managers)
        await Data_collector_states.admin_manager.set()


@dp.message_handler(Command("add_manager"), state=Data_collector_states.admin_manager)
async def add_manager(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)

    text = "Выберите <b>город</b>, в который вы хотите <b>добавить</b> менеджера. \n \n <b>Для возврата в основное меню введите</b> /back"
    list_of_cities = await keyboard.cities_keyboard()
    await message.answer(text=text, reply_markup=list_of_cities)
    await Data_collector_states.admin_add_manager_city.set()


@dp.message_handler(Text, state=Data_collector_states.admin_add_manager_city)
async def add_manager_city(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    city = message.text
    await state.update_data(manager_city=city)
    stores = await keyboard.stores_keyboard(city)
    text = "Выберите <b>название</b> магазина в который вы хотите <b>добавить</b> менеджера. \n \n <b>Для возврата в основное меню введите</b> /back"

    await message.answer(text=text, reply_markup=stores)
    await Data_collector_states.admin_add_manager_store.set()


@dp.message_handler(Text, state=Data_collector_states.admin_add_manager_store)
async def add_manager_store(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    manager_store_name = message.text
    await state.update_data(manager_store=manager_store_name)
    text = """Введите <b>имя менеджера</b>, которого вы хотите <b>добавить</b>.

Имя <b>должно</b> быть в <b>формате</b> <b>IVAN.IVANOV</b>.
<b>Имя и фамилия заглавными латинскими буквами и через точку (.)</b>.

<b>Для возврата в основное меню введите</b> /back"""
    await message.answer(text=text, reply_markup=keyboard.ReplyKeyboardRemove())
    await Data_collector_states.admin_add_manager_name.set()


@dp.message_handler(Text, state=Data_collector_states.admin_add_manager_name)
async def add_manager_name(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    manager_name = message.text
    await state.update_data(manager_name=manager_name)
    text = """Введите <b>Telegram username</b> менеджера.
<b>USERNAME нужно ввести без @!</b>

<b>Для возврата в основное меню введите</b> /back"""

    await message.answer(text=text)
    await Data_collector_states.admin_add_manager_username.set()


@dp.message_handler(Text, state=Data_collector_states.admin_add_manager_username)
async def add_manager_username(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    data = await state.get_data()
    manager_city = data.get("manager_city")
    manager_store = data.get("manager_store")
    manager_name = data.get("manager_name")
    manager_username = message.text
    chat_id = await tg_bot_database.admin_manager_query("INSERT", manager_city, manager_store, manager_name,
                                                        manager_username)
    if chat_id != 'not set':
        await bot.send_message(chat_id, "Вам обновили права. Введите /restart")
    text = """Менеджер <b>добавлен</b> в базу данных.

Для <b>работы с магазинами</b> нажмите <b>Stores</b>.
Для <b>работы с менеджерами</b> нажмите <b>Managers</b>.
Для <b>работы с сотрудниками</b> нажмите <b>Workers</b>.
"""
    await message.answer(text=text, reply_markup=keyboard.admin_keyboard)
    await Data_collector_states.admin_waiting.set()


@dp.message_handler(Command("delete_manager"), state=Data_collector_states.admin_manager)
async def delete_manager(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    text = "Выберите <b>город</b>, в котором вы хотите <b>удалить</b> менеджера. \n \n <b>Для возврата в основное " \
           "меню введите</b> /back "
    list_of_cities = await keyboard.cities_keyboard()
    await message.answer(text=text, reply_markup=list_of_cities)
    await Data_collector_states.admin_delete_manager_city.set()


@dp.message_handler(Text, state=Data_collector_states.admin_delete_manager_city)
async def delete_manager_city(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    city = message.text
    await state.update_data(manager_city=city)
    text = "Выберите <b>название</b> магазина, в котором вы хотите <b>удалить</b> менеджера. \n \n <b>Для возврата в " \
           "основное меню введите</b> /back "
    stores = await keyboard.stores_keyboard(city)
    await message.answer(text=text, reply_markup=stores)
    await Data_collector_states.admin_delete_manager_store.set()


@dp.message_handler(Text, state=Data_collector_states.admin_delete_manager_store)
async def delete_manager_store(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    manager_store_name = message.text
    await state.update_data(manager_store=manager_store_name)
    data = await state.get_data()
    city = data.get("manager_city")
    managers = await keyboard.users_list(city, manager_store_name, "Manager")
    text = "Выберите имя менеджера, которого вы хотите <b>удалить.</b> \n \n <b>Для возврата в основное меню " \
           "введите</b> /back "
    await message.answer(text=text, reply_markup=managers)
    await Data_collector_states.admin_delete_manager_name.set()


@dp.message_handler(Text, state=Data_collector_states.admin_delete_manager_name)
async def delete_manager_name(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    data = await state.get_data()
    manager_city = data.get("manager_city")
    manager_store = data.get("manager_store")
    manager_name = message.text
    chat_id = await tg_bot_database.admin_manager_query("DELETE", manager_city, manager_store, manager_name)
    if chat_id != 'not set':
        await bot.send_message(chat_id, "Вам обновили права. Введите /restart")
    text = """Менеджер <b>удален</b> из базы данных

Для <b>работы с магазинами</b> нажмите <b>Stores</b>.
Для <b>работы с менеджерами</b> нажмите <b>Managers</b>.
Для <b>работы с сотрудниками</b> нажмите <b>Workers</b>."""

    await message.answer(text=text, reply_markup=keyboard.admin_keyboard)
    await Data_collector_states.admin_waiting.set()


@dp.message_handler(Text("Workers"), state=Data_collector_states.admin_waiting)
async def admin_workers_options(message: Message):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    user_data = await tg_bot_database.check_if_registered(message.from_user.username)
    if user_data:
        text = """Для <b>добавления работника</b> нажмите /add_worker
Для <b>удаления работника</b> нажмите /delete_worker

<b>Для возврата в основное меню введите</b> /back"""
        await message.answer(text=text, reply_markup=keyboard.admin_workers)
        await Data_collector_states.admin_worker.set()


@dp.message_handler(Command("add_worker"), state=Data_collector_states.admin_worker)
async def add_worker(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    text = "Выберите <b>город</b>, в который вы хотите <b>добавить</b> работника. \n \n <b>Для возврата в основное меню введите</b> /back"
    list_of_cities = await keyboard.cities_keyboard()
    await message.answer(text=text, reply_markup=list_of_cities)
    await Data_collector_states.admin_add_worker_city.set()


@dp.message_handler(Text, state=Data_collector_states.admin_add_worker_city)
async def add_worker_city(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    city = message.text
    await state.update_data(worker_city=city)
    stores = await keyboard.stores_keyboard(city)
    text = "Выберите <b>название магазина</b>, в который вы хотите <b>добавить</b> работника. \n \n <b>Для возврата в основное меню введите</b> /back"

    await message.answer(text=text, reply_markup=stores)
    await Data_collector_states.admin_add_worker_store.set()


@dp.message_handler(Text, state=Data_collector_states.admin_add_worker_store)
async def add_worker_store(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    worker_store_name = message.text
    await state.update_data(worker_store=worker_store_name)
    text = """Введите <b>имя работника</b>, которого вы хотите <b>добавить</b>.
Имя <b>должно</b> быть в <b>формате</b> <b>IVAN.IVANOV</b>.
<b>Имя и фамилия заглавными латинскими буквами и через точку (.)</b>.

<b>Для возврата в основное меню введите</b> /back"""
    await message.answer(text=text, reply_markup=keyboard.ReplyKeyboardRemove())
    await Data_collector_states.admin_add_worker_name.set()


@dp.message_handler(Text, state=Data_collector_states.admin_add_worker_name)
async def add_worker_name(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    worker_name = message.text
    await state.update_data(worker_name=worker_name)
    text = """Введите <b>Telegram username</b> сотрудника.
<b>Username нужно ввести без @!</b>

<b>Для возврата в основное меню введите</b> /back"""
    await message.answer(text=text)
    await Data_collector_states.admin_add_worker_username.set()


@dp.message_handler(Text, state=Data_collector_states.admin_add_worker_username)
async def add_worker_username(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    data = await state.get_data()
    worker_city = data.get("worker_city")
    worker_store = data.get("worker_store")
    worker_name = data.get("worker_name")
    worker_username = message.text
    chat_id = await tg_bot_database.admin_worker_query("INSERT", worker_city, worker_store, worker_name, worker_username)
    if chat_id != 'not set':
        await bot.send_message(chat_id, "Вам обновили права. Введите /restart")
    text = """Работник <b>добавлен</b> в базу данных

Для <b>работы с магазинами</b> нажмите <b>Stores</b>.
Для <b>работы с менеджерами</b> нажмите <b>Managers</b>.
Для <b>работы с сотрудниками</b> нажмите <b>Workers</b>.
"""
    await message.answer(text=text, reply_markup=keyboard.admin_keyboard)
    await Data_collector_states.admin_waiting.set()


@dp.message_handler(Command("delete_worker"), state=Data_collector_states.admin_worker)
async def delete_worker(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    text = "Выберите <b>город</b>, в котором вы хотите удалить работника. \n \n <b>Для возврата в основное меню введите</b> /back"
    list_of_cities = await keyboard.cities_keyboard()
    await message.answer(text=text, reply_markup=list_of_cities)
    await Data_collector_states.admin_delete_worker_city.set()


@dp.message_handler(Text, state=Data_collector_states.admin_delete_worker_city)
async def delete_worker_city(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    city = message.text
    await state.update_data(worker_city=city)
    stores = await keyboard.stores_keyboard(city)
    text = "Выберите <b>название магазина</b>, в котором вы хотите <b>удалить</b> работника. \n \n <b>Для возврата в " \
           "основное меню введите</b> /back "

    await message.answer(text=text, reply_markup=stores)
    await Data_collector_states.admin_delete_worker_store.set()


@dp.message_handler(Text, state=Data_collector_states.admin_delete_worker_store)
async def delete_worker_store(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    data = await state.get_data()
    worker_city = data.get("worker_city")
    worker_store_name = message.text
    await state.update_data(worker_store=worker_store_name)
    list_of_workers = await keyboard.users_list(worker_city, worker_store_name, "Worker")
    text = "<b>Выберите работника</b>, которого вы хотите удалить. \n \n <b>Для возврата в основное меню введите</b> " \
           "/back "
    await message.answer(text=text, reply_markup=list_of_workers)
    await Data_collector_states.admin_delete_worker_name.set()


@dp.message_handler(Text, state=Data_collector_states.admin_delete_worker_name)
async def delete_worker_name(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    data = await state.get_data()
    worker_city = data.get("worker_city")
    worker_store = data.get("worker_store")
    worker_name = message.text
    chat_id = await tg_bot_database.admin_worker_query("DELETE", worker_city, worker_store, worker_name)
    if chat_id != 'not set':
        await bot.send_message(chat_id, "Вам обновили права. Введите /restart")
    text = """Работник <b>удален</b> из базы данных

Для <b>работы с магазинами</b> нажмите <b>Stores</b>.
Для <b>работы с менеджерами</b> нажмите <b>Managers</b>.
Для <b>работы с сотрудниками</b> нажмите <b>Workers</b>.
"""
    await message.answer(text=text, reply_markup=keyboard.admin_keyboard)
    await Data_collector_states.admin_waiting.set()


@dp.message_handler(Command("add_admin"), state=Data_collector_states.admin_waiting)
async def add_admin(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    user_data = await tg_bot_database.check_if_registered(message.from_user.username)
    if user_data["rights"] == 'Super Admin':
        text = """Введите username пользователя, которого вы хотите сделать супер админом
Username нужно ввести без @.

<b>Для возврата в основное меню введите</b> /back"""
        await message.answer(text=text, reply_markup=keyboard.admin_keyboard)
        await Data_collector_states.super_admin_add_admin.set()
    else:
        text = """Данная команда не доступна вам."""
        await message.answer(text=text)


@dp.message_handler(Text, state=Data_collector_states.super_admin_add_admin)
async def add_admin_username(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    username = message.text
    chat_id = await tg_bot_database.super_admin_query("UPDATE", username)
    if chat_id != 'not set':
        await bot.send_message(chat_id, "Вам обновили права. Введите /restart")
    text = """Вы сделали пользователя админом.

Для <b>работы с магазинами</b> нажмите <b>Stores</b>.
Для <b>работы с менеджерами</b> нажмите <b>Managers</b>.
Для <b>работы с сотрудниками</b> нажмите <b>Workers</b>."""
    await message.answer(text=text, reply_markup=keyboard.admin_keyboard)
    await Data_collector_states.admin_waiting.set()


@dp.message_handler(Command("delete_admin"), state=Data_collector_states.admin_waiting)
async def delete_admin(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    user_data = await tg_bot_database.check_if_registered(message.from_user.username)
    if user_data["rights"] == 'Super Admin':
        text = """Введите username пользователя, у которого вы хотите забрать права админа.
Username нужно ввести без @.

<b>Для возврата в основное меню введите</b> /back"""
        await message.answer(text=text, reply_markup=keyboard.admin_keyboard)
        await Data_collector_states.super_admin_delete_admin.set()
    else:
        text = """Данная команда вам не доступна"""
        await message.answer(text=text)


@dp.message_handler(Text, state=Data_collector_states.super_admin_delete_admin)
async def delete_admin_username(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    username = message.text
    chat_id = await tg_bot_database.super_admin_query("DELETE", username)
    if chat_id != 'not set':
        await bot.send_message(chat_id, "Вам обновили права. Введите /restart")
    text = """Вы удалили пользователя из базы админов.

Для <b>работы с магазинами</b> нажмите <b>Stores</b>.
Для <b>работы с менеджерами</b> нажмите <b>Managers</b>.
Для <b>работы с сотрудниками</b> нажмите <b>Workers</b>."""
    await message.answer(text=text, reply_markup=keyboard.admin_keyboard)
    await Data_collector_states.admin_waiting.set()
