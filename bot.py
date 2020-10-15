import telebot

bot = telebot.TeleBot("1348161215:AAHLT_cdj2657dPdKG0CmZAesqbRL6DHP94")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет! Вас приветствует Mafia Bonds')

@bot.message_handler(commands=["rules", "Правила"])
def send_rules(message):
   @bot.message_handler(commands=['rules', 'Правила'])
    msg = bot.send_message(message.chat.id, 'https://telegra.ph/Pravila-igry-09-08-4')

if __name__ == "__main__":    
    bot.polling()
