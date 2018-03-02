import config
import telebot
import datetime
import bs4
import requests
from telebot import types
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def get_start(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_summer = types.KeyboardButton(text="Сколько дней до лета?")
    button_today = types.KeyboardButton(text = "Скажи погоду на сегодня")
    button_tor = types.KeyboardButton(text = "Скажи погоду на завтра")
    button_help = types.KeyboardButton(text="/help")
    keyboard.add(button_summer, button_today,button_tor, button_help)
    bot.send_message(message.chat.id,"Я забагованная хреновина, не ругайся, может что и смогу",
                     reply_markup=keyboard)


@bot.message_handler(func = lambda msg: msg.text == 'Сколько дней до лета?')
def get_summer(message):
    a = ["2018", "06", "01"]
    try:
        bot.send_message(message.chat.id, "До лета: " +  ' '.join(str(datetime.date(int(a[0]),int(a[1]),int(a[2])) - datetime.date.today() ).split()[0:2])
    + " уважаемый @"  + message.chat.username)
    except TypeError:
        bot.send_message(message.chat.id, "До лета: " + ' '.join(
            str(datetime.date(int(a[0]), int(a[1]), int(a[2])) - datetime.date.today()).split()[0:2])
                         + " уважаемый " + message.chat.first_name)


@bot.message_handler(func = lambda msg: msg.text == 'Скажи погоду на сегодня')
def get_today(message):
    s = requests.get('https://www.meteoservice.ru/weather/text/moskva')
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p3 = b.select('.words p')
    bot.send_message(message.chat.id, p3[0].getText())


@bot.message_handler(func = lambda msg: msg.text == 'Скажи погоду на завтра')
def get_tor(message):
    s = requests.get('https://www.meteoservice.ru/weather/text/moskva')
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p3 = b.select('.words p')
    bot.send_message(message.chat.id, p3[1].getText())



@bot.message_handler(commands=["help"])
def get_summer(message):
    bot.send_message(message.chat.id,
                     "привет, холодный кусок мяса, "
                     "я подарю тебе надежду в этом ледяном аду, "
                     "я подарю тебе веру в то, что рано или поздно придёт тепло")

if __name__ == '__main__':
    bot.polling(none_stop=True)
1
