import telebot
import re
import requests
import os

API_TOKEN = os.environ.get("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = message
    bot.reply_to(msg,  
     f"Hi {msg.chat.first_name}!\n\n"
        "I'm link Unshortener bot. Just send me link and get shortened link.\n\n Created By @steallootdeal"
    )

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    msgs = message.text
    Links = (re.search("(?P<url>https?://[^\s]+)", msgs).group("url"))
    Link = [re.search("(?P<url>https?://[^\s]+)", msgs).group("url")][0]
    session = requests.Session()  # so connections are recycled
    resp = session.head(Link, allow_redirects=True)
    output = resp.url
    txt = (msgs.replace(Links, str(output)))
    bot.reply_to(message, txt, disable_web_page_preview=True)


bot.infinity_polling()

# session = requests.Session()  # so connections are recycled
# resp = session.head(url, allow_redirects=True)
# print(resp.url)