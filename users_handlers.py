from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from main import dp, bot
from states import Data_collector_states
import eventlog
import tg_bot_database
import keyboard


@dp.message_handler(Command("input_number"), state= Data_collector_states.waiting_for_customer_number)
async def ask_customer_number(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    user_data = await tg_bot_database.check_if_registered(message.from_user.username)
    if user_data:
        text = """Введите номер абонента в формате 70000000000.
Номер должен состоять из одинацати цифр. +7 и 8 вводить не нужно."""
        await message.answer(text=text, reply_markup=keyboard.ReplyKeyboardRemove())
        await Data_collector_states.customer_number_input.set()


@dp.message_handler(Text, state=Data_collector_states.customer_number_input)
async def customer_number_input(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    customer_number = message.text
    message_id = message.message_id
    chat_id = message.chat.id
    username_tg = message.from_user.username
    if customer_number.isdigit() and len(customer_number) == 11 and customer_number[0] == '7':
        message_date = message.date
        customer_number_data = (customer_number, message_date, username_tg)
        await tg_bot_database.insert_to_customer_number_table(*customer_number_data)
        result = await eventlog.select_data_from_eventlog_database(customer_number)
        if result:
            await tg_bot_database.update_90_days_status_customer_number_table(customer_number, message_date, result)
        text = """Спасибо! Номер зарегистрирован.
Для регистрации абонента введите команду /input_number"""
        await message.answer(text=text, reply_markup=keyboard.user_keyboard)
        await bot.delete_message(chat_id, message_id)
        await Data_collector_states.waiting_for_customer_number.set()
    else:
        text = """Номер абонента введен неверно!
Введите команду /input_number, а затем верный номер"""
        await bot.delete_message(chat_id, message_id)
        await message.answer(text=text, reply_markup=keyboard.user_keyboard)



