#!/usr/bin/env python3
"""
All skills relating wikipedia.
"""

import wikipedia
from telegram.ext import CommandHandler


class WikipediaSkills:

    """Skills to search for information on wikipedia."""

    def __init__(self, dispatcher):
        wikipedia.set_lang("de")
        # Last used or searched pageid by the user.
        self.last_pageid = {}
        # current_topic.get(chat_id, None) returns None if chat_id doesn't exist as key

        dispatcher.add_handler(CommandHandler('wiki', self.get_article))

    def get_article(self, bot, update):
        """Searches for an article with the given name.
        If not found it suggests article names or tells
        that nothing was found"""
        chat_id = update.message.chat_id
        query = update.message.text.split(' ', 1)[1]

        response = ""
        try:
            page = wikipedia.page(title=query)
            self.last_pageid[chat_id] = page.pageid
            response = page.title + "\n\n" + \
                page.summary
            # TODO: acc sections later here.
        except wikipedia.exceptions.PageError:
            # couldn't associate a wikipedia article with the query
            suggestions = wikipedia.search(query, results=5)
            response = "Konnte keinen zugehörigen Wikipedia " + \
                "Artikel finden. Hier ein paar Vorschläge:\n" + \
                ', \n'.join(suggestions)

        bot.send_message(chat_id=chat_id, text=response)
