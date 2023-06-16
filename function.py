
from verbform import dictionary, russian_list
from bot import bot


#Поиск по инфинитиву глагола на русском языке
def ru_search(message):
    (message.text).lower()
    if ((message.text).lower() in russian_list):
        for key, value in dictionary.items():
            if (message.text).lower() in value:
                bot.send_message(message.chat.id,f'{key}')
                if (key in list((dictionary.keys()))):
                    answer = dictionary[key]
                    bot.send_message(message.chat.id, f"Перевод: {answer[0]}\n"
                                                      f"Настоящее время, 3 лицо единственное число: {answer[1]}\n"
                                                      f"Простое прошедшее время, 3 лицо единственное число: {answer[2]}\n"
                                                      f"Перфект: {answer[3]}")
        bot.send_message(message.chat.id, f'Выбери команду')
    else:
        bot.send_message(message.chat.id, f'Я не знаю такого слова, или глагол правильный')
        bot.send_message(message.chat.id, f'Выбери команду')


#Поиск по инфинитиву глагола на немецком языке
def de_search(message):
    request = (message.text).lower()
    if request in dictionary.keys():
        answer = dictionary[request]
        bot.send_message(message.chat.id, f"Перевод: {answer[0]}\n"
                                          f"Настоящее время, 3 лицо единственное число: {answer[1]}\n"
                                          f"Простое прошедшее время, 3 лицо единственное число: {answer[2]}\n"
                                          f"Перфект: {answer[3]}")
    else:
        bot.send_message(message.chat.id, f'Я не знаю такого слова, или глагол правильный')
        bot.send_message(message.chat.id, f'Выбери команду')

    bot.send_message(message.chat.id, f'Выбери команду')