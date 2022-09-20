"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

import settings
import ephem

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(update, context):
    text = update.message.text
    print (text)
    update.message.reply_text(text)

def input_planet(update, context):
    text = update.message.text.split(' ')[1]
    if text == "Mars":
      const = ephem.constellation(ephem.Mars('2022-09-21'))
    if text == "Venus":
      const = ephem.constellation(ephem.Venus('2022-09-21'))
    if text == "Mercury":
      const = ephem.constellation(ephem.Mercury('2022-09-21'))
    if text == "Jupiter":
      const = ephem.constellation(ephem.Jupiter('2022-09-21'))
    if text == "Saturn":
      const = ephem.constellation(ephem.Saturn('2022-09-21'))
    if text == "Uranus":
      const = ephem.constellation(ephem.Uranus('2022-09-21'))
    if text == "Neptune":
      const = ephem.constellation(ephem.Neptune('2022-09-21'))
    update.message.reply_text(const)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", input_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
