import telebot
from time import time

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
    link = '[Как стать амдином? Посмотрите статью!](https://telegra.ph/Kak-stat-adminom-v-Mafia-Bonds-09-27)'
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



GROUP_ID = -1001212001029  # ID вашей группы

strings = {
    "ru": {
        "ro_msg": "Вам запрещено отправлять сюда сообщения за оскорбления в течение 10 минут."
    },
    "en": {
        "ro_msg": "You're not allowed to send messages here for 10 minutes."
    }
}
   
def get_language(lang_code):
    # Иногда language_code может быть None
    if not lang_code:
        return "en"
    if "-" in lang_code:
        lang_code = lang_code.split("-")[0]
    if lang_code == "ru":
        return "ru"
    else:
        return "en"


# Удаляем сообщения с ссылками
@bot.message_handler(func=lambda message: message.entities is not None and message.chat.id == GROUP_ID)
def delete_links(message):
    for entity in message.entities:
        if entity.type in ["url", "text_link"]:
            bot.delete_message(message.chat.id, message.message_id)
        else:
            return



restricted_messages = ["@", "t.me/", "http", "https", "ебанутый", "шлюха", "хуесос", "еблан"]


@bot.message_handler(func=lambda message: message.text and message.text.lower() in restricted_messages and message.chat.id == GROUP_ID)
def set_ro(message):
    bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time()+600)
    bot.send_message(message.chat.id, strings.get(get_language(message.from_user.language_code)).get("ro_msg"),
                     reply_to_message_id=message.message_id)
'''
------------------------------------------------------------
'''


if __name__ == "__main__":    
    bot.polling()

