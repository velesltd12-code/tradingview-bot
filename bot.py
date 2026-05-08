from telegram.ext import ApplicationBuilder
from flask import Flask, request
import asyncio
import threading

TOKEN = "8423163106:AAE9g1L_8Gx11MzYb40BUBD4soP-p1nXado"
CHAT_ID = "412895025"

app_flask = Flask(__name__)
bot_app = ApplicationBuilder().token(TOKEN).build()

@app_flask.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', 'Сигнал от TradingView')
    asyncio.run(send_message(message))
    return 'OK', 200

async def send_message(text):
    await bot_app.bot.send_message(chat_id=CHAT_ID, text=text)

if __name__ == '__main__':
    app_flask.run(host='0.0.0.0', port=8080)
