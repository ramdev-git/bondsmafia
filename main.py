from aiogram import Bot, Dispatcher, types, executor
from aiogram import *
from aiogram.types import *

import config


boty = Bot(token=config.token)
dp = Dispatcher(boty)

inline_kb_full = InlineKeyboardMarkup()
inline_kb_full.add(InlineKeyboardButton('Правила чата', url='https://telegra.ph/Pravila-igry-11-09'))

dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    if message['from'].id in config.admins_id:
        await message.answer(f"Привет Админ!")
    elif message['from'].id in config.creator_id:
    	await message.answer(f'Ку создатель ))))')
    else:
        await message.answer(f"Привет, {message['from'].first_name}!\nВас приветствует Mafia Bonds!\nРады видеть Вас в чате, оставайтесь с нами. Прочитайте, пожалуйста, правила чата!", reply_markup=inline_kb_full)

 
@dp.message_handler(content_types=['new_chat_members'])
async def start_command(message: types.Message):
    if message['from'].id in config.admins_id:
        await message.answer(f"Привет Админ!")
    elif message['from'].id in config.creator_id:
    	await message.answer(f'Ку создатель ))))')
    else:
await message.answer(f"Привет, {message['from'].first_name}!\nВас приветствует Mafia Bonds!\nРады видеть Вас в чате, оставайтесь с нами. Прочитайте, пожалуйста, правила чата!", reply_markup=inline_kb_full)


@dp.message_handler(commands=['help'])
async def help_commnand(message: types.Message):
    await message.answer("Чтобы получать наши сообщения в настройках приватности добавьте бота в исключения: Настройки>Конфиденциальность>Пересылка сообщений>Добавить исключения")

        
@dp.message_handler()
async def adminnn(message: types.Message):
    if message.reply_to_message == None:
        for admins_list in config.admins_id:
            if '/start' not in message.text:
                await boty.forward_message(admins_list, message.from_user.id, message.message_id)
            elif '/help' not in message.text:
                await boty.forward_message(admins_list, message.from_user.id, message.message_id)

    else:
        if message['from'].id in config.admins_id:
            if message.reply_to_message.forward_from.id:
                await boty.send_message(message.reply_to_message.forward_from.id, message.text)
        else:
            await message.answer('Нельзя отвечать на сообщения. Напишите в личные сообщения.')


@dp.message_handler(content_types=['document', 'photo', 'video', 'audio', 'sticker', 'voice'])
async def handle_content_typ(message):
    for admins_list in config.admins_id:
        await boty.forward_message(admins_list, message.from_user.id, message.message_id)

'''
@dp.message_handler(content_types=['new_chat_members'])
async def new_member(message):
    await message.answer(f'Привет!', reply_markup=inline_kb_full)
'''   

@dp.message_handler(content_types=['location'])
async def reply_to_pers(message):
    await message.answer(f'Ок, скинь еще номер ❤️')


if __name__ == '__main__':
    executor.start_polling(dp)
