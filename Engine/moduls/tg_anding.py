from Engine.information import starter_check as sc
import telebot
from telebot import types
from . import func
import sys

bot = telebot.TeleBot(token=sc.TOKEN_TG)

button_check = telebot.types.KeyboardButton('Перевiрити борг')
button_sell = telebot.types.KeyboardButton('Упаковка')
button_add = telebot.types.KeyboardButton('Продаж')
check_btn = telebot.types.KeyboardButton('Перевiрити iсторiю')
strt = telebot.types.KeyboardButton("/start")

start_kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(strt)
greet_kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=False)
greet_kb.row(button_check)
greet_kb.add(button_sell, button_add)
greet_kb.row(check_btn)

bot.send_message('1439133134', "Я живий.", reply_markup=start_kb)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    if message.from_user.id == 1439133134:
        msg = bot.send_message(message.from_user.id, "Я живий.", reply_markup=greet_kb)
        bot.register_next_step_handler(msg, func.check)



@bot.message_handler(commands=['rld'])
def send_welcome(message):
    if message.from_user.id == "1439133134":
        bot.send_message(message.from_user.id, "Програму буде перезавантажено.", reply_markup=greet_kb)
        sc.os.execl(sys.executable, sys.executable, *sys.argv)



bot.infinity_polling()