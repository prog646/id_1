from settings import TOKEN
import telebot


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def forward_mes(message):
    if message.chat.username == 'themax646':
        msg = message.text
        data_chat = ['-351947292']
        i = 0
        while i < len(data_chat):
            bot.send_message(data_chat[i], msg)
            i += 1
    else:
        print('Ошибка')


bot.polling()