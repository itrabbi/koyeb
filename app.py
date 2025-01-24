from flask import Flask
import threading
from main import start_bot
from pymongo import MongoClient
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/')
def home():
    return "Wow, bot is ok", 200
    
@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200

if __name__ == "__main__":
    threading.Thread(target=start_bot).start()
    app.run(host='0.0.0.0', port=8080)
