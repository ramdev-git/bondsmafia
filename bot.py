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
      bot.send_message(message.chat.id, "🙋Добро пожаловать {0.first_name}!\n⚙️Доступные команды можно узнать через /help".format(message.from_user, bot.get_me()))
    
@bot.message_handler(commands=["rules", "Правила"])
def send_rules(message):
    link = '[Правила чата](https://telegra.ph/Pravila-igry-09-08-4)'
    bot.send_message(message.chat.id, link, parse_mode='MarkdownV2')
    
@bot.message_handler(commands=["FAQ", "Как играть"])
def send_rules(message):
    link = '[Как играть? -> Посмотрите в этой статье <-](https://telegra.ph/FAQ-po-igre-v-Mafiyu-09-23)'
    bot.send_message(message.chat.id, link, parse_mode='MarkdownV2')
)'
                               
@bot.message_handler(commands=["help", "Справка"])
def send_rules(message):
    bot.send_message(message.chat.id, 'Доступные команды:\n /rules\n  ')

if __name__ == "__main__":    
    bot.polling()
https://telegra.ph/FAQ-po-igre-v-Mafiyu-09-23
