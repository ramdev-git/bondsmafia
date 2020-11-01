from aiogram import Bot, Dispatcher, executor, types
from aiogram import *
from aiogram.types import *


TOKEN = "1472805654:AAHTOeNeusZOSqE4eMC7J66lb0v4Dqyyoz0"
admin_id = 1355949068
admin_id = 1383795967


boty = Bot(token=TOKEN)
dp = Dispatcher(boty)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
  if message['from'].id == admin_id:
    await message.answer(f"Привет Админ!")
  else:
    await message.answer(f"Привет, {message['from'].first_name}! Бот для         обратной связи. Напиши и мы скоро ответим")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
  await message.answer('@Mrfire7')

    
@dp.message_handler()
async def process_start_command(message: types.Message):
  if message.reply_to_message == None:
    if '/start' not in message.text:
      await boty.forward_message(admin_id, message.from_user.id,           message.message_id)
    elif '/help' not in message.text:
      await boty.forward_message(admin_id, message.from_user.id,           message.message_id)
  else:
    if message['from'].id == admin_id:
      if message.reply_to_message.forward_from.id:
        await boty.send_message(message.reply_to_message.forward_from.id,             message.text)
    else:
      await message.answer('Нельзя отвечать на сообщения.')


      
@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
  await boty.forward_message(admin_id, message.from_user.id, message.message_id)

  
@dp.message_handler(content_types=['document'])
async def handle_docs_photo(message):
  await boty.forward_message(admin_id, message.from_user.id, message.message_id)

  
if __name__ == '__main__':
  executor.start_polling(dp)
