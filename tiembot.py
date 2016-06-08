#!/usr/bin/env python3
"""
TiemBot. Where everything gets put together.
"""

from telegram.ext import Updater, CommandHandler

from skills.wikipedia_skills import WikipediaSkills


class TiemBot:

    """This is the Tiem Bot.
    It puts together all the different skills into one bot."""

    def __init__(self, token):
        """Sets up the bot."""
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher

        self.dispatcher.add_handler(CommandHandler('start', start))

        WikipediaSkills(self.dispatcher)

    def start_bot(self):
        """The bot will start responding to messages."""
        self.updater.start_polling()
        self.updater.idle()


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="I'm a bot, please talk to me! This bot is created by JonnyTiem")
