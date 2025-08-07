import telebot
import json
from config import BOT_TOKEN, NOWPAYMENTS_API_KEY, WALLETS

bot = telebot.TeleBot(BOT_TOKEN)

# Load stock data
def load_stock():
    with open("stock.json", "r") as f:
        return json.load(f)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Casino Account Shop! Type /stock to see available accounts.")

@bot.message_handler(commands=['stock'])
def show_stock(message):
    stock = load_stock()
    msg = "Available Casino Accounts:\n"
    for account in stock["casino_accounts"]:
        msg += f"- {account['name']}: {account['price']} {account['currency']} ({account['stock']} in stock)\n"
    bot.reply_to(message, msg)

@bot.message_handler(commands=['wallets'])
def show_wallets(message):
    msg = "Accepted Crypto Wallets:\n"
    for coin, addr in WALLETS.items():
        msg += f"- {coin}: `{{addr}}`\n"
    bot.reply_to(message, msg, parse_mode="Markdown")

# Add more handlers as required...

if __name__ == "__main__":
    bot.polling()