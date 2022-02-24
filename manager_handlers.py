from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from main import dp, bot
from states import Data_collector_states
import tg_bot_database
import eventlog
import keyboard


@dp.message_handler(Command("add_employee"), state=Data_collector_states.manager_waiting)
async def input_new_name(message: Message):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    user_data = await tg_bot_database.check_if_registered(message.from_user.username)
    if user_data:
        text = """Введите имя сотрудника в формате IVAN.IVANOV
Имя и фамилия заглавными латинскими буквами и через точку (.)."""

        await message.answer(text=text, reply_markup=keyboard.ReplyKeyboardRemove())
        await Data_collector_states.manager_add_employee.set()


@dp.message_handler(Text, state=Data_collector_states.manager_add_employee)
async def input_new_username(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    new_name = message.text
    await state.update_data(employee_name=new_name)
    text = """Введите Telegram username сотрудника.
USERNAME нужно ввести без @! 
"""

    await message.answer(text=text)
    await Data_collector_states.manager_add_username_employee.set()


@dp.message_handler(Text, state=Data_collector_states.manager_add_username_employee)
async def add_employee(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    data = await state.get_data()
    employee_username = message.text
    employee_name = data.get("employee_name")
    manager_username = message.from_user.username
    await tg_bot_database.manager_query("INSERT", employee_name, manager_username, employee_username=employee_username)
    text = """Спасибо!
Сотрудник добавлен в базу данных.

Для добавления нового сотрудника нажмите /add_employee
Для удаления сотрудника нажмите /delete_employee

Для регистрации абонентов введите команду /input_number"""

    await message.answer(text=text, reply_markup=keyboard.manager_keyboard)
    await Data_collector_states.manager_waiting.set()


@dp.message_handler(Command("delete_employee"), state=Data_collector_states.manager_waiting)
async def delete_name(message: Message):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    user_data = await tg_bot_database.check_if_registered(message.from_user.username)
    if user_data:
        text = """Вы удаляете сотрудника из базы.
Выберите имя сотрудника."""
        employee_list = await keyboard.users_list(user_data['city'], user_data['office'], 'Worker')
        await message.answer(text=text, reply_markup=employee_list)
        await Data_collector_states.manager_delete_employee.set()


@dp.message_handler(state=Data_collector_states.manager_delete_employee)
async def delete_employee(message: Message):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    employee_name = message.text
    manager_username = message.from_user.username
    await tg_bot_database.manager_query("DELETE", employee_name, manager_username)
    text = """Спасибо!
Сотрудник удален из базы данных.

Для добавления нового сотрудника нажмите /add_employee
Для удаления сотрудника нажмите /delete_employee

Для регистрации абонентов введите команду /input_number"""

    await message.answer(text=text, reply_markup=keyboard.manager_keyboard)
    await Data_collector_states.manager_waiting.set()


@dp.message_handler(Command("input_number"), state=Data_collector_states.manager_waiting)
async def ask_customer_number(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    user_data = await tg_bot_database.check_if_registered(message.from_user.username)
    if user_data:
        text = """Введите номер абонента в формате 70000000000.
Номер должен состоять из одинацати цифр. +7 и 8 вводить не нужно."""
        await message.answer(text=text, reply_markup=keyboard.ReplyKeyboardRemove())
        await Data_collector_states.manager_customer_number_input.set()


@dp.message_handler(Text, state=Data_collector_states.manager_customer_number_input)
async def customer_number_input(message: Message, state: FSMContext):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    customer_number = message.text
    message_id = message.message_id
    chat_id = message.chat.id
    username_tg = message.from_user.username
    if customer_number.isdigit() and len(customer_number) == 11 and customer_number[0] == '7':
        message_date = message.date.date()
        customer_number_data = (customer_number, message_date, username_tg)
        await tg_bot_database.insert_to_customer_number_table(*customer_number_data)
        result = await eventlog.select_data_from_eventlog_database(customer_number)
        if result:
            await tg_bot_database.update_90_days_status_customer_number_table(customer_number, message_date, result)
        text = """Спасибо!
Номер добавлен в базу данных.

Для добавления нового сотрудника нажмите /add_employee
Для удаления сотрудника нажмите /delete_employee

Для регистрации абонентов введите команду /input_number"""
        await message.answer(text=text, reply_markup=keyboard.user_keyboard)
        await bot.delete_message(chat_id, message_id)
    else:
        text = """Номер абонента введен неверно!
Введите команду /input_number, а затем верный номер"""
        await bot.delete_message(chat_id, message_id)
        await message.answer(text=text, reply_markup=keyboard.manager_keyboard)
    await Data_collector_states.manager_waiting.set()

