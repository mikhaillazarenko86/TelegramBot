from telebot import types
from bot import *
from function import ru_search, de_search




@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Помощь")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я помогу тебе разобраться в 3 формах неправильных глаголов".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Помощь"):
        bot.send_message(message.chat.id, text="Привет. Спасибо, что выбрал меня! Нажми кнопку Задать вопрос, а затем выбери нужную команду. Удачи")
    elif (message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Инфинитив ru")
        btn2 = types.KeyboardButton("Инфинитив de")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "Инфинитив ru"):
        bot.send_message(message.chat.id, "Напиши на русском инфинитив глагола и я подскажу тебе три его формы")
        bot.register_next_step_handler(message, ru_search)

    elif message.text == "Инфинитив de":
        bot.send_message(message.chat.id, text="Напиши на немецком инфинитив глагола и я подскажу тебе три его формы")
        bot.register_next_step_handler(message, de_search)
    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Помощь")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую команду я не запрограммирован.")


bot.polling(none_stop=True)