import telebot
from time import time
from telebot import types
from aiogram import Bot, Dispatcher, executor, types
from aiogram import *
from aiogram.types import *

bot = telebot.TeleBot("1472805654:AAHTOeNeusZOSqE4eMC7J66lb0v4Dqyyoz0")
'''
bot = telebot.TeleBot("1348161215:AAHLT_cdj2657dPdKG0CmZAesqbRL6DHP94")
'''
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет! Вас приветствует Mafia Bonds')
@bot.message_handler(content_types=['new_chat_members'])
def handle_docs_audio(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Правила чата", url="https://telegra.ph/Pravila-igry-09-08-4")
    urls_button = types.InlineKeyboardButton(text="Как играть", url="https://telegra.ph/FAQ-po-igre-v-Mafiyu-09-23")
    urlp_button = types.InlineKeyboardButton(text="Как стать админом", url="https://telegra.ph/Kak-stat-adminom-v-Mafia-Bonds-09-27")
    keyboard.add(url_button)
    keyboard.add(urls_button)
    keyboard.add(urlp_button)
    bot.send_message(message.chat.id, "🙋Добро пожаловать, {0.first_name}!\n⚙️Доступные команды можно узнать через /help".format(message.from_user, bot.get_me()), reply_markup=keyboard,)
    
@bot.message_handler(commands=["rules"])
def send_rules(message):
    link = '[Правила чата](https://telegra.ph/Pravila-igry-09-08-4)'
    bot.send_message(message.chat.id, link, parse_mode='MarkdownV2')
    
@bot.message_handler(commands=["faq"])
def send_rules(message):
    link = '[Как играть? Посмотрите в этой статье](https://telegra.ph/FAQ-po-igre-v-Mafiyu-09-23)'
    bot.send_message(message.chat.id, link, parse_mode='MarkdownV2')
	
	
@bot.message_handler(commands=["admins"])
def send_rules(message):
    link = '[Как стать адмиином? Посмотрите статью](https://telegra.ph/Kak-stat-adminom-v-Mafia-Bonds-09-27)'
    bot.send_message(message.chat.id, link, parse_mode='MarkdownV2')

                               
@bot.message_handler(commands=["help"])
def send_rules(message):
    bot.send_message(message.chat.id, 'Доступные команды:\n /rules - Показывает ссылку на правила этого чата\n /faq - Показывает ссылку на статью как играть в мафию\n /id - Показывает айди вашего профиля\n /admins - Как стать админом?\n')
    
@bot.message_handler(commands=['id'])
def send_start(message):
    bot.send_message(message.chat.id, 'Твой ID: ' + str(message.from_user.id))

'''
-----------------------------------------------------------------------------------------
'''




TOKEN = "1472805654:AAHTOeNeusZOSqE4eMC7J66lb0v4Dqyyoz0"
admin_id = 1355949068


boty = Bot(token=TOKEN)
dp = Dispatcher(boty)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	if message['from'].id == admin_id:
		await message.answer(f"Привет Админ!")
	else:
		await message.answer(f"Привет, {message['from'].first_name}! Бот для 				обратной связи.")

		
@dp.message_handler()
async def process_start_command(message: types.Message):
	if message.reply_to_message == None:
		if '/start' not in message.text:
			await boty.forward_message(admin_id, message.from_user.id, 					message.message_id)
	else:
		if message['from'].id == admin_id:
			if message.reply_to_message.forward_from.id:
				await boty.send_message(message.reply_to_message.forward_from.id, 						message.text)
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


'''
------------------------------------------------------------
'''


if __name__ == "__main__":    
    bot.polling()

