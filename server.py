#!/usr/bin/env python3

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Filters

import RPi.GPIO as GPIO
import time
import config
import logging

pin = 17

updater = Updater(config.api_token)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  level=logging.INFO)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.LOW)


def open(bot, update):
  GPIO.output(pin, GPIO.HIGH)
  time.sleep(4)
  GPIO.output(pin, GPIO.LOW)
  bot.send_message(chat_id=update.message.chat_id, text="Welcome!")

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id,
    text="""Hi!
    To open the door say /open.
    To get access your Telegram ID has to be whitelisted.
    You can get your ID by contacting @myidbot.""")

def status(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="Still alive.")

def main():
  try:
    dispatcher.add_handler(
      CommandHandler("start", start))
    dispatcher.add_handler(
      CommandHandler("status", status))
    dispatcher.add_handler(
      CommandHandler("open", open, Filters.chat(config.allowed_chat_ids)))

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

    updater.start_polling()
    updater.idle()
  finally:
    GPIO.cleanup()

if __name__ == "__main__":
  main()
