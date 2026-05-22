import telebot
from flask import Flask
from threading import Thread
from apscheduler.schedulers.background import BackgroundScheduler

from config import BOT_TOKEN
from utils.scheduler import kick_expired_users

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="Markdown")

app = Flask(__name__)

@app.route('/')
def home():
    return "BNF BOT RUNNING"


def run_web():
    app.run(host="0.0.0.0", port=10000)


def keep_alive():
    Thread(target=run_web).start()


if __name__ == '__main__':

    keep_alive()

    scheduler = BackgroundScheduler()

    scheduler.add_job(
        kick_expired_users,
        'interval',
        minutes=1
    )

    scheduler.start()

    print("BNF BOT STARTED")

    bot.infinity_polling(skip_pending=True)
