from telebot import TeleBot
from telebot import apihelper

from app import config


apihelper.proxy = {'https': 'socks5://proxyuser:rOOOtof8DOTnet@ec2-35-161-119-34.us-west-2.compute.amazonaws.com:1080'}
bot = TeleBot(config.TOKEN)
