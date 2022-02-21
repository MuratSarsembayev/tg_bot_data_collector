from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from main import tg_bot_database

user_keyboard = ReplyKeyboardMarkup([["/input_number"]], resize_keyboard=True)

manager_keyboard = ReplyKeyboardMarkup([["/add_employee"], ["/delete_employee"], ["/input_number"]],
                                       resize_keyboard=True)
admin_keyboard = ReplyKeyboardMarkup([["Stores"], ["Managers"], ["Workers"]], resize_keyboard=True)

admin_stores = ReplyKeyboardMarkup([["/add_store"], ["/delete_store"]], resize_keyboard=True)

admin_managers = ReplyKeyboardMarkup([["/add_manager"], ["/delete_manager"]], resize_keyboard=True)

admin_workers = ReplyKeyboardMarkup([["/add_worker"], ["/delete_worker"]], resize_keyboard=True)


async def cities_keyboard():
    cities_list = await tg_bot_database.cities()
    cities_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for item in cities_list:
        cities_kb.add(item)
    return cities_kb


async def stores_keyboard(city):
    list_of_stores = await tg_bot_database.stores(city)
    stores_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for item in list_of_stores:
        stores_kb.add(item)
    return stores_kb


async def users_list(city, store, rights):
    list_of_users = await tg_bot_database.get_list(city, store, rights)
    users_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for item in list_of_users:
        users_kb.add(item)
    return users_kb
