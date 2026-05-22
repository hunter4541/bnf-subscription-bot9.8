import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread
from apscheduler.schedulers.background import BackgroundScheduler

from config import BOT_TOKEN

# ---------------- BOT SETUP ---------------- #

bot = telebot.TeleBot(
    BOT_TOKEN,
    parse_mode="Markdown"
)

# ---------------- FLASK KEEP ALIVE ---------------- #

app = Flask(__name__)

@app.route('/')
def home():
    return "BNF BOT RUNNING"


def run_web():
    app.run(
        host="0.0.0.0",
        port=10000
    )


def keep_alive():
    Thread(target=run_web).start()

# ---------------- AUTO TASKS ---------------- #

def auto_tasks():
    print("Running background tasks...")

# ---------------- START COMMAND ---------------- #

@bot.message_handler(commands=['start'])
def start_message(message):

    markup = InlineKeyboardMarkup(row_width=1)

    markup.add(
        InlineKeyboardButton(
            "💳 28 Days — ₹399",
            callback_data="plan_399"
        )
    )

    markup.add(
        InlineKeyboardButton(
            "💎 Lifetime — ₹1999",
            callback_data="plan_lifetime"
        )
    )

    markup.add(
        InlineKeyboardButton(
            "📞 Contact Admin",
            url="https://t.me/YOUR_USERNAME"
        )
    )

    text = (
        "🔥 *WELCOME TO BNF PRIVATE COMMUNITY*\n\n"
        "📈 Premium Trading Community\n\n"
        "✅ Daily Market Analysis\n"
        "✅ Live Trading Sessions\n"
        "✅ Premium Trade Setups\n"
        "✅ Risk Management\n"
        "✅ Community Support\n\n"
        "━━━━━━━━━━━━━━\n\n"
        "💳 Select your subscription plan below"
    )

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=markup
    )

# ---------------- BUTTON CALLBACKS ---------------- #

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    
    if call.data == "plan_399":

        bot.answer_callback_query(call.id)

        bot.send_message(
            call.message.chat.id,
            "💳 Payment system coming next..."
        )

    elif call.data == "plan_lifetime":

        bot.answer_callback_query(call.id)

        bot.send_message(
            call.message.chat.id,
            "💎 Lifetime plan selected."
        )

# ---------------- START BOT ---------------- #

if __name__ == '__main__':

    keep_alive()

    scheduler = BackgroundScheduler()

    scheduler.add_job(
        auto_tasks,
        'interval',
        minutes=1
    )

    scheduler.start()

    print("BNF BOT STARTED")

    bot.infinity_polling(
        skip_pending=True
    )
