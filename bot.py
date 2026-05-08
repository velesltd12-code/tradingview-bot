import requests
from flask import Flask, request, jsonify

TOKEN = "8423163106:AAE9g1L_8Gx11MzYb40BUBD4soP-p1nXado"
CHAT_ID = "412895025"

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', 'Сигнал от TradingView')
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": message})
    return jsonify({'status': 'ok'}), 200

@app.route('/', methods=['GET'])
def index():
    return 'Bot is running!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
