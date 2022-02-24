from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from main import dp, bot
from states import Data_collector_states
import keyboard
import tg_bot_database


@dp.message_handler(Command("start"), state=None)
async def start_chat(message: Message):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    user_data = await tg_bot_database.check_if_registered(message.from_user.username)
    if user_data:
        await tg_bot_database.user_tg_data_update(message.from_user.username, str(message.chat.id),
                                                  str(message.from_user.id))
        if user_data["rights"] == 'Worker':
            text = "Добро пожаловать в систему регистрации новых пользователей <b>SuperApp!</b>\nВы уже <b>зарегистрированы.</b> " \
                   "\nДля <b>регистрации абонентов</b> введите команду /input_number "

            await message.answer(text=text, reply_markup=keyboard.user_keyboard)
            await Data_collector_states.waiting_for_customer_number.set()

        elif user_data["rights"] == 'Manager':
            text = """Добро пожаловать в систему регистрации новых пользователей <b>SuperApp!</b>
Для <b>добавления</b> нового сотрудника нажмите /add_employee
Для <b>удаления сотрудника</b> нажмите /delete_employee
Для <b>регистрации</b> абонентов введите команду /input_number"""

            await message.answer(text=text, reply_markup=keyboard.manager_keyboard)
            await Data_collector_states.manager_waiting.set()
        elif user_data["rights"] == 'Admin' or user_data["rights"] == 'Super Admin':
            text = "Добро пожаловать в систему регистрации новых пользователей SuperApp!\nДля <b>работы с " \
                   "магазинами</b> " \
                   "нажмите " \
                   "<b>Stores</b>.\nДля <b>работы с менеджерами</b> нажмите <b>Managers</b>.\bДля <b>работы с " \
                   "сотрудниками</b> нажмите <b>Workers</b>. "

            await message.answer(text=text, reply_markup=keyboard.admin_keyboard)
            await Data_collector_states.admin_waiting.set()
    else:
        text = """Извините. Бот вам недоступен."""
        await message.answer(text=text)
        await Data_collector_states.finish.set()


@dp.message_handler(Command("back"), state='*')
async def back(message: Message):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    user_data = await tg_bot_database.check_if_registered(message.from_user.username)
    if user_data:
        if user_data["rights"] == 'Worker':
            text = "Для <b>регистрации абонентов</b> введите команду /input_number "

            await message.answer(text=text, reply_markup=keyboard.user_keyboard)
            await Data_collector_states.waiting_for_customer_number.set()

        elif user_data["rights"] == 'Manager':
            text = """Для <b>добавления</b> нового сотрудника нажмите /add_employee
Для <b>удаления сотрудника</b> нажмите /delete_employee
Для <b>регистрации</b> абонентов введите команду /input_number"""

            await message.answer(text=text, reply_markup=keyboard.manager_keyboard)
            await Data_collector_states.manager_waiting.set()
        elif user_data["rights"] == 'Admin' or user_data["rights"] == 'Super Admin':
            text = """Для <b>работы с магазинами</b> нажмите <b>Stores</b>.
Для <b>работы с менеджерами</b> нажмите <b>Managers</b>.
Для <b>работы с сотрудниками</b> нажмите <b>Workers</b>. """

            await message.answer(text=text, reply_markup=keyboard.admin_keyboard)
            await Data_collector_states.admin_waiting.set()
    else:
        text = """Извините. Бот вам недоступен."""
        await message.answer(text=text)
        await Data_collector_states.finish.set()


@dp.message_handler(Command("restart"), state='*')
async def back(message: Message):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    user_data = await tg_bot_database.check_if_registered(message.from_user.username)
    if user_data:
        if user_data["rights"] == 'Worker':
            text = "Для <b>регистрации абонентов</b> введите команду /input_number "

            await message.answer(text=text, reply_markup=keyboard.user_keyboard)
            await Data_collector_states.waiting_for_customer_number.set()

        elif user_data["rights"] == 'Manager':
            text = """Для <b>добавления</b> нового сотрудника нажмите /add_employee
Для <b>удаления сотрудника</b> нажмите /delete_employee
Для <b>регистрации</b> абонентов введите команду /input_number"""

            await message.answer(text=text, reply_markup=keyboard.manager_keyboard)
            await Data_collector_states.manager_waiting.set()
        elif user_data["rights"] == 'Admin' or user_data["rights"] == 'Super Admin':
            text = """Для <b>работы с магазинами</b> нажмите <b>Stores</b>.
Для <b>работы с менеджерами</b> нажмите <b>Managers</b>.
Для <b>работы с сотрудниками</b> нажмите <b>Workers</b>. """

            await message.answer(text=text, reply_markup=keyboard.admin_keyboard)
            await Data_collector_states.admin_waiting.set()
    else:
        text = """Извините. Бот вам недоступен."""
        await message.answer(text=text)
        await Data_collector_states.finish.set()
