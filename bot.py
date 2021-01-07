from aiogram import Bot, Dispatcher, executor, types
from aiogram import *
from aiogram.types import *


TOKEN = "1570534929:AAHArisiocKoipSqLOhMvf9eKMD5Fs_7TiI"
# 980646747

admins = [897053725, 1355949068]

boty = Bot(token=TOKEN)
dp = Dispatcher(boty)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
  if message['from'].id in admins:
    await message.answer(f"Привет Админ!")
  else:
    await message.answer(f"Привет, {message['from'].first_name}! Бот для обратной связи. Мы получаем и читаем все ваши сообщения, но не всем можем овтетить. \nПросьба, выключите пожалуйста у себя в настройках\"Пересылка сообщений\" или добавьте бота в исключения. Рекомендуем второй вариант")


@dp.message_handler(commands=['help'])
async def help_commnand(message: types.Message):
  await message.answer(" \nЗа спам получите спам ;)")

    
@dp.message_handler()
async def adminnn(message: types.Message):
  if message.reply_to_message == None:
    for admins_list in admins:
      if '/start' not in message.text:
        await boty.forward_message(admins_list, message.from_user.id, message.message_id)
      elif '/help' not in message.text:
        await boty.forward_message(admins_list, message.from_user.id, message.message_id)

  else:
    if message['from'].id in admins:
      if message.reply_to_message.forward_from.id:
        await boty.send_message(message.reply_to_message.forward_from.id, message.text)
    else:
      await message.answer('Нельзя отвечать на сообщения.')


'''@dp.message_handler(content_types=['document', 'photo', 'video', 'audio', 'sticker', 'voice'])
async def handle_content_typ(message):
  for admins_list in admins:
    await boty.forward_message(admins_list, message.from_user.id, message.message_id)
'''

@dp.message_handler(content_types=['new_chat_members'])
async def new_member(message):
  await message.answer(f'Привет, {message['from'].first_name}!')
  
@dp.message_handler(content_types=['location'])
async def reply_to_pers(message):
  await message.answer(f'Ок, скинь еще номер ')

if __name__ == '__main__':
  executor.start_polling(dp)
