import telebot

import config
from verbform import verbform


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши инфинитив глагола и я подскажу тебе три его формы)')
#Поиск слов
@bot.message_handler(content_types=["text"])
def findvebform(message):
    if message.text in list((verbform.keys())):
        answer = verbform[message.text]
        # bot.send_message(message.chat.id, str(verbform[message.text]))
        bot.send_message(message.chat.id, f"Перевод: {answer[0]}\n"
                                          f"Настоящее время, 3 лицо единственное число: {answer[1]}\n"
                                          f"Простое прошедшее время, 3 лицо единственное число:: {answer[2]}\n"
                                          f"Перфект: {answer[2]}")
    else:
        bot.send_message(message.chat.id, "Я не знаю")
#Игра на запоминание перевода
@bot.message_handler(commands=["play"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Давай проверим как хорошо ты запомнил перевод глаголов. Я пишу тебе на русском, а ты мне инфинитив на немецком.)')

# RUN
bot.polling(none_stop=True)
