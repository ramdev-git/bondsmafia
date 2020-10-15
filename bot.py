import telebot
bot = telebot.TeleBot("1214001983:AAE-VmGC4SK6bGg4nXUvHtlm2ArsPKWsG1s")
'''
bot = telebot.TeleBot("1348161215:AAHLT_cdj2657dPdKG0CmZAesqbRL6DHP94")
'''
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет! Вас приветствует Mafia Bonds')
@bot.message_handler(content_types=['new_chat_members'])
def handle_docs_audio(message):
	bot.send_message(message.chat.id, 'Привет')
    
@bot.message_handler(commands=["rules", "Правила"])
def send_rules(message):
    bot.send_message(message.chat.id, 'https://telegra.ph/Pravila-igry-09-08-4')

if __name__ == "__main__":    
    bot.polling()
