import config
import telebot
import datetime
import bs4
import requests
from telebot import types
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start", "home"])
def get_start(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_summer = types.KeyboardButton(text="Сколько дней до лета?")
    button_today = types.KeyboardButton(text = "Скажи погоду на сегодня")
    button_tor = types.KeyboardButton(text = "Скажи погоду на завтра")
    button_anyday = types.KeyboardButton(text = "Скажи погоду на какой нибудь-другой день")
    button_help = types.KeyboardButton(text="/help")
    keyboard.add(button_summer, button_today,button_tor, button_help, button_anyday)
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


@bot.message_handler(func = lambda msg: msg.text == 'Скажи погоду на какой нибудь-другой день')
def get_tor(message):
    config.flag_day = True
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    button_0 = types.KeyboardButton(text="0")
    button_1 = types.KeyboardButton(text="1")
    button_2 = types.KeyboardButton(text="2")
    button_3 = types.KeyboardButton(text="3")
    button_4 = types.KeyboardButton(text="4")
    button_5 = types.KeyboardButton(text="5")
    button_6 = types.KeyboardButton(text="6")
    button_7 = types.KeyboardButton(text="7" )
    button_7 = types.KeyboardButton(text="/home")
    keyboard.add(button_0,button_1,button_2,
                 button_3,button_4,button_5,
                 button_6,button_7)
    bot.send_message(message.chat.id, "на сколько дней тебе показать погоду?",
                     reply_markup=keyboard)

@bot.message_handler(func = lambda msg: config.flag_day == True)
def days(message):
    s = requests.get('https://www.meteoservice.ru/weather/text/moskva')
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p3 = b.select('.words p')
    h3 = b.select('.text_forecast h3')
    bot.send_message(message.chat.id,h3[int(message.text)].getText()+ '\n'+ p3[int(message.text)].getText())


@bot.message_handler(commands=["help"])
def get_summer(message):
    bot.send_message(message.chat.id,
                     "привет, холодный кусок мяса, "
                     "я подарю тебе надежду в этом ледяном аду, "
                     "я подарю тебе веру в то, что рано или поздно придёт тепло")

if __name__ == '__main__':
    bot.polling(none_stop=True)
