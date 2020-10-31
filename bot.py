

from aiogram import Bot, Dispatcher, executor, types
from aiogram import *
from aiogram.types import *

# 1472805654:AAHTOeNeusZOSqE4eMC7J66lb0v4Dqyyoz0 token
TOKEN = "1311410269:AAFaabFYx6SZV-fXsEscz1lLMySNpfyvZoA"
admin_id = 897053725


boty = Bot(token=TOKEN)
dp = Dispatcher(boty)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	if message['from'].id == admin_id:
		await message.answer(f"Привет Админ!")
	else:
		await message.answer(f"Привет, {message['from'].first_name}! Вас приветствует Mafia Bonds")


@dp.message_handler(commands=['help'])
async def group_faq(message:types.Message):
	await message.answer(f'Доступные команды:\n /rules - Показывает ссылку на правила этого чата\n /faq - Показывает ссылку на статью как играть в мафию\n /admin - Как стать админом?\n')


@dp.message_handler(commands=['rules'])
async def group_rules(message: types.Message):
	rules_inl_keyb = InlineKeyboardMarkup()
	rules_inl_keyb.add(InlineKeyboardButton('Правила чата', url='https://telegra.ph/Pravila-igry-09-08-4'))
	await message.answer(f"Наши правила:", reply_markup=rules_inl_keyb)


@dp.message_handler(commands=['faq'])
async def group_faq(message:types.Message):
	faq_inl_keyb = InlineKeyboardMarkup()
	faq_inl_keyb.add(InlineKeyboardButton('FAQ', url='https://telegra.ph/FAQ-po-igre-v-Mafiyu-09-23'))
	await message.answer(f'Справка', reply_markup=faq_inl_keyb)


@dp.message_handler(commands=['admin'])
async def how_to_be_admin(message:types.Message):
	adm_inl_keyb = InlineKeyboardMarkup()
	adm_inl_keyb.add(InlineKeyboardButton('Статья', url='https://telegra.ph/Kak-stat-adminom-v-Mafia-Bonds-09-27'))
	await message.answer(f'Как стать адмиином? Посмотрите статью', reply_markup=adm_inl_keyb)


		
@dp.message_handler()
async def process_start_command(message: types.Message):
	if message.reply_to_message == None:
		if '/start' not in message.text:
			await boty.forward_message(admin_id, message.from_user.id, message.message_id)


	else:
		if message['from'].id == admin_id:
			if message.reply_to_message.forward_from.id:
				await boty.send_message(message.reply_to_message.forward_from.id, message.text)
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
