from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from src.config import *
import requests
from bs4 import BeautifulSoup


class Bot:
    def __init__(self, token):
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher
        self.job_queue = self.updater.job_queue
        # create handlers
        self.start_handler = CommandHandler('start', self.start)
        self.stop_handler = CommandHandler('stop', self.stop)
        self.message_handler = MessageHandler([Filters.text], self.handle_message)
        # add handlers
        self.dispatcher.add_handler(self.start_handler)
        self.dispatcher.add_handler(self.message_handler)

    def run(self):
        self.updater.start_polling()
        self.updater.idle()

    @staticmethod
    def start(dispatcher, update, **kwargs):
        dispatcher.sendMessage(chat_id=update.message.chat_id, text="Hello there! Start sending me receipts!")

    def stop(self):
        self.job_queue.stop()

    def error(update, error_obj, err):
        logger.info('Update "%s" caused error "%s" and "%s"' % (update, error_obj, err))

    @staticmethod
    def handle_message(dispatcher, update, **kwargs):
        if FOOD_DICTIONARY_URL in update.message.text:
            # parse the receipt
            try:
                for li in BeautifulSoup(requests.get(update.message.text).text, 'html.parser').find_all("li"):
                    name = li.find("span", {'property': 'v:name'})
                    amount = li.find("span", {'property': 'v:amount'})
                    if name and amount:
                        dispatcher.sendMessage(chat_id=update.message.chat_id, text="{}\n".format(name.text))
            except Exception as e:
                logger.exception(e)