import telebot

bot = telebot.TeleBot("1348161215:AAHLT_cdj2657dPdKG0CmZAesqbRL6DHP94")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет! Вас приветствует Mafia Bonds')

@bot.message_handler(commands=["rules", "Правила"])
def send_rules(message):
    bot.send_message(message.chat.id, 'Тест')

if __name__ == "__main__":    
    bot.polling()
