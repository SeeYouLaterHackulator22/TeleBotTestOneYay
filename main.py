import os
import telebot
from replit import db

API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")

@bot.message_handler(commands=['Hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello there!")

bot.polling()
