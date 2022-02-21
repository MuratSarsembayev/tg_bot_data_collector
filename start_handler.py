from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from main import dp
from states import Data_collector_states
import keyboard
from tg_bot_database import tg_bot_database


@dp.message_handler(Command("start"), state=None)
async def start_chat(message: Message):
    await tg_bot_database.log(message.from_user.username, message.date, message.text)
    user_data = await tg_bot_database.check_if_registered(message.from_user.username)
    if user_data:
        if user_data["rights"] == 'Worker':
            text = "Добро пожаловать в систему регистрации новых пользователей <b>SuperApp!</b>\nВы уже <b>зарегистрированы.</b> " \
                   "\nДля регистрации абонентов введите команду /input_number "

            await message.answer(text=text, reply_markup=keyboard.user_keyboard)
            await Data_collector_states.waiting_for_customer_number.set()

        elif user_data["rights"] == 'Manager':
            text = "Добро пожаловать в систему регистрации новых пользователей <b>SuperApp!</b>\nДля " \
                   "<b>добавления</b> нового " \ 
                   "сотрудника нажмите /add_employee\nДля <b>удаления сотрудника нажмите</b> /delete_employee\n\nДля " \
                   "<b>регистрации</b> " \ 
                   "абонентов введите команду /input_number "

            await message.answer(text=text, reply_markup=keyboard.manager_keyboard)
            await Data_collector_states.manager_waiting.set()
        elif user_data["rights"] == 'Admin' or user_data["rights"] == 'Super Admin':
            text = "Добро пожаловать в систему регистрации новых пользователей SuperApp!\nДля работы с магазинами " \
                   "нажмите " \
                   "Stores.\nДля работы с менеджерами нажмите Managers.\bДля работы с сотрудниками нажмите Workers. "

            await message.answer(text=text, reply_markup=keyboard.admin_keyboard)
            await Data_collector_states.admin_waiting.set()
    else:
        text = """Извините. Бот вам недоступен."""
        await message.answer(text=text)
        await Data_collector_states.finish.set()
