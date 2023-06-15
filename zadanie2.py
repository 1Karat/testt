import telebot

import random


token = '6102086665:AAFIFWr6h2kOP0uxH09m57iCcT-5fIh_W9Y'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = """
    Привет! Я умею рассказывать стихи, знаю много интересных фактов и могу показать милых котиков!
    """
    bot.send_message(message.chat.id,  welcome_text)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворенье..."
    bot.send_message(message.chat.id, poem_text)


@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_number = str(random.randint(1,10))
    cat_img = open('img/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)

@bot.message_handler(commands=['random_game'])
def send_advice(message):
    games = ['Dota', 'StarCraft II', 'CS:GO']
    game = random.choice(1,3)
    print(game)
    bot.send_message(message.chat.id,games)

bot.polling()
