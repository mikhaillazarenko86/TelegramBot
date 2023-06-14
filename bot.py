import telebot
import config
from verbform import dictionary, russian_list
from telebot import types


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи.')
#Поиск слов
@bot.message_handler(commands=["show"])
def show(message):
    bot.send_message(message.chat.id, 'Напиши на немецком инфинитив глагола и я подскажу тебе три его формы')
    findvebform
@bot.message_handler(content_types=['text'])
def findvebform(message):
    if message.text in list((dictionary.keys())):
        answer = dictionary[message.text]
        # bot.send_message(message.chat.id, str(verbform[message.text]))
        bot.send_message(message.chat.id, f"Перевод: {answer[0]}\n"
                                          f"Настоящее время, 3 лицо единственное число: {answer[1]}\n"
                                          f"Простое прошедшее время, 3 лицо единственное число:: {answer[2]}\n"
                                          f"Перфект: {answer[2]}")
    elif message.text == '/start':
        start(message, res=False)
    elif message.text == '/play':
        play(message,res=False)
    elif message.text == '/showru':
        show_ru_start(message)
    else:
        bot.send_message(message.chat.id, "Я не знаю")
#Поиск инфинитива глагола по русскому инфинитиву
@bot.message_handler(commands=["showru"])
def show_ru_start(message):
    bot.send_message(message.chat.id, 'Напиши на русском инфинитив глагола и я подскажу тебе три его формы')
    show_ru(message)
@bot.message_handler(content_types=['text'])
def show_ru(message):
    if message.text in russian_list:
        for key, value in dictionary.items():
            if message.text in value:
                print(key)
    elif message.text == '/start':
        start(message, res=False)
    elif message.text == '/play':
        play(message,res=False)
    else:
        print('Я не знаю')
#Игра на запоминание перевода
@bot.message_handler(commands=["play"])
def play(m, res=False):
    bot.send_message(m.chat.id, 'Давай проверим как хорошо ты запомнил перевод глаголов. Я пишу тебе на русском, а ты мне инфинитив на немецком.)')

# RUN
bot.polling(none_stop=True)
