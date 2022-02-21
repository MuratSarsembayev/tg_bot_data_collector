import asyncio
import aioschedule

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import bot_token, work_sheet
from eventlog import scheduled_get_data_from_eventlog

import tg_bot_database

loop = asyncio.get_event_loop()
bot = Bot(bot_token, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())


async def update_superapp_user_status():
    customer_numbers = await tg_bot_database.scheduled_get_not_superapp_user_customer_number_table()
    numbers_from_eventlog = await scheduled_get_data_from_eventlog(customer_numbers)
    updated_data = await tg_bot_database.scheduled_update_users_superapp_status(numbers_from_eventlog)
    work_sheet.clear()
    updated_data.columns = ['Отметка о времени', 'Город', 'Магазин', 'ФИО', 'Номер', '90 дней', 'Стал ли пользователем']
    work_sheet.set_dataframe(updated_data, start=(1, 1))


async def scheduler():
    aioschedule.every().day.at("08:00").do(update_superapp_user_status)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
