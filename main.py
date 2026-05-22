import telebot
from flask import Flask
from threading import Thread
from apscheduler.schedulers.background import BackgroundScheduler

from config import BOT_TOKEN

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

@bot.message_handler(commands=['start'])
def start_message(message):

    text = (
        "🔥 *WELCOME TO BNF PRIVATE COMMUNITY*\n\n"
        "📈 Premium Trading Community\n\n"
        "✅ Daily Market Analysis\n"
        "✅ Live Trading Sessions\n"
        "✅ Premium Trade Setups\n"
        "✅ Risk Management\n"
        "✅ Community Support\n\n"
        "━━━━━━━━━━━━━━\n\n"
        "💳 Select your plan below"
    )

    bot.send_message(
        message.chat.id,
        text
    )
    print("BNF BOT STARTED")

    bot.infinity_polling(skip_pending=True)
