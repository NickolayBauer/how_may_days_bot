import config
import telebot
import datetime
from telebot import types
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start", "leto"])
def get_start(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_summer = types.KeyboardButton(text="Сколько дней до лета?")
    button_help = types.KeyboardButton(text="/help")
    keyboard.add(button_summer, button_help)
    bot.send_message(message.chat.id,
                     "Помогу тебе посчитать, сколько дней осталось до лета",
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


@bot.message_handler(commands=["help"])
def get_help(message):
    bot.send_message(message.chat.id,
                     "привет, холодный кусок мяса, "
                     "я подарю тебе надежду в этом ледяном аду, "
                     "я подарю тебе веру в то, что рано или поздно придёт тепло")

@bot.message_handler(content_types=["text"])
def get_text(message):
    bot.send_message(message.chat.id,
                     "Просто введи /leto и я помогу тебе узнать дни до него")

if __name__ == '__main__':
    bot.polling(none_stop=True)
