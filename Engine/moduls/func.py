from Engine.information.starter_check import *
from . import tg_anding
import time


def check(message):
    global db_info
    if message.text == "Перевiрити борг":
        g = 0
        conn = sqlite3.connect(os.path.join(PATH, 'information', 'db.db'))
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM dolg''')
        db_info = cursor.fetchall()
        conn.close()
        for i in db_info:
            g += i[1]
        msg = tg_anding.bot.send_message(message.from_user.id, f'Заборжнiсть рiвняеться: {g} грв.', reply_markup=tg_anding.greet_kb)
        tg_anding.bot.register_next_step_handler(msg, check)
    elif message.text == "Упаковка":
        tg_anding.bot.send_message(message.from_user.id, "Введiть кiлькiсть.", reply_markup=tg_anding.telebot.types.ReplyKeyboardRemove())
        msg = tg_anding.bot.send_message(message.from_user.id, "(0 - вiдмiнити)")
        tg_anding.bot.register_next_step_handler(msg, add_two)
    elif message.text == "Продаж":
        tg_anding.bot.send_message(message.from_user.id, "Введiть вартiсть продажу.", reply_markup=tg_anding.telebot.types.ReplyKeyboardRemove())
        msg = tg_anding.bot.send_message(message.from_user.id, "(0 - вiдмiнити)")
        tg_anding.bot.register_next_step_handler(msg, sell_dolg)
    elif message.text == "Перевiрити iсторiю":
        txt = ''
        conn = sqlite3.connect(os.path.join(PATH, 'information', 'db.db'))
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM dolg''')
        db_info = cursor.fetchall()
        conn.close()
        db_info.reverse()
        for i in db_info:
            if i[0] == 1:
                p1 = 'Упаковка'
            elif i[0] == 2:
                p1 = 'Продаж'
            txt += f'{p1} - {i[1]} грв. Додано - {i[2]}\n'
        msg = tg_anding.bot.send_message(message.from_user.id, txt, reply_markup=tg_anding.greet_kb)
        tg_anding.bot.register_next_step_handler(msg, check)

def add_two(message):
    try:
        answ = int(message.text)
    except:
        msg = tg_anding.bot.send_message(message.from_user.id, "Введiть кiлькiсть ЧИСЛОМ (0 - вiдмiнити)", reply_markup=tg_anding.telebot.types.ReplyKeyboardRemove())
        tg_anding.bot.register_next_step_handler(msg, add_two)
    finally:
        if answ:
            bobs_time = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime())
            for i in range(answ):
                insert_num(bobs_time)
            msg = tg_anding.bot.send_message(message.from_user.id, "Записав. Можете продовжувати займатися справами.", reply_markup = tg_anding.greet_kb)
            tg_anding.bot.register_next_step_handler(msg, check)
        else:
            msg = tg_anding.bot.send_message(message.from_user.id, "Окей, вiдмiнив.", reply_markup = tg_anding.greet_kb)
            tg_anding.bot.register_next_step_handler(msg, check)

def sell_dolg(message):
    try:
        answ = int(message.text)
    except:
        msg = tg_anding.bot.send_message(message.from_user.id, "Введiть вартiсть ЧИСЛОМ (0 - вiдмiнити)", reply_markup=tg_anding.telebot.types.ReplyKeyboardRemove())
        tg_anding.bot.register_next_step_handler(msg, add_two)
    finally:
        if answ:
            bobs_time = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime())
            answ = int(answ / 100 * 2 // 1)
            insert_num(bobs_time, 2, answ)
            msg = tg_anding.bot.send_message(message.from_user.id, "Записав. Можете продовжувати займатися справами.", reply_markup = tg_anding.greet_kb)
            tg_anding.bot.register_next_step_handler(msg, check)
        else:
            msg = tg_anding.bot.send_message(message.from_user.id, "Окей, вiдмiнив.", reply_markup = tg_anding.greet_kb)
            tg_anding.bot.register_next_step_handler(msg, check)