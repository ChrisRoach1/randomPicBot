import telebot
from random import randrange
import config

keywords = ['Name','Sign','Nature','Internet', 'Typing', 'Wireless', 'Telephone', 'Network', 'Screen', 'Person',
            'Iphone', 'Android', 'Laptop', 'App', 'Monitor', 'Computer', 'Apple', 'Phone', 'Code', 'Text', 'Animal',
            'Girl', 'Wildlife', 'Captive', 'Programming', 'Wild', 'Seal', 'Building', 'City', 'Safari', 'Wild Animal',
            'Wallpaper', 'Love', 'Boy', 'Business', 'Man', 'Food', 'Landscape', 'Flowers', 'Health', 'House', 'Happy',
            'Question', 'Quotes', 'Coffee', 'Coffee shop', 'Green', 'Blue', 'Red', 'Purple', 'Pink', 'Lake', 'Tree']


bot = telebot.TeleBot(config.api['key'])

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "/help will list out all possible commands for the bot")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, "Enter a choice to begin\n"
                          "/pixel \n"
                          "/oneplue \n"
                          "/iphoneX ")

@bot.message_handler(commands=['iphoneX'])
def iphoneX_image(message):
    random_index = randrange(0, len(keywords)-1)
    random_keyword = keywords[random_index]
    url = 'https://source.unsplash.com/random/1579x2890/?{}'.format(random_keyword)
    bot.reply_to(message, url)

@bot.message_handler(commands=['pixel'])
def iphoneX_image(message):
    random_index = randrange(0, len(keywords)-1)
    random_keyword = keywords[random_index]
    url = 'https://source.unsplash.com/random/1440x2560/?{}'.format(random_keyword)
    bot.reply_to(message, url)

@bot.message_handler(commands=['oneplus'])
def iphoneX_image(message):
    random_index = randrange(0, len(keywords)-1)
    random_keyword = keywords[random_index]
    url = 'https://source.unsplash.com/random/1080x1920/?{}'.format(random_keyword)
    bot.reply_to(message, url)

@bot.message_handler(func= lambda message: message.text == 'rick and morty time')
def rick_and_morty(message):
	bot.reply_to(message, 'https://steamusercontent-a.akamaihd.net/ugc/863988638213732922/F0A10005B74BCBCCCB224EB0F2C94ED93AD740DB/')


bot.polling()
