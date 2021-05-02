import os
import dotenv as dv
import random

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


class Sentences:
    """Storage for all sentences the bot can throw out"""

    insult_texts = ["Du stinkst hart nach Maggi.", "Fettsack geh sport machen!", "Ein Baum hat mehr IQ als du.",
               "Waschlappen.", "Ich habe kein Fett bestellt.", "Du Null.", "Du CDU Wähler.",
               "Ich hoffe deine Eltern versaufen das Kindergeld.", "Du Windows User.", "Flasche.",
               "Dich will ich nicht sehen.", "Toll, jetzt hab ich Augenkrebs von dir."]

    other = ["Hier könnte ihr Werbung stehen", "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
             "MACH DAS SAUBER!", "Tschüss"]

    insult_answers = ["Anzeige ist raus.", "Hurensohn", "Das ist nicht nett du Hurensohn."]

    insults = ["hurensohn", "arsch", "pisser", "wichser"]


def start(update, context):
    """Command /start"""
    update.message.reply_text("Booting up my booty.")

def help(update, context):
    """Command /help"""
    update.message.reply_text("Bei dir ist jegliche Hilfe verloren.")

def msg_replys(update, context):
    """Text replys"""
    hello_answers = Sentences.insult_texts + Sentences.other
    insult_answers = Sentences.insult_texts + Sentences.insult_answers

    message = update.message.text.lower()

    if message == "hallo" or message == "hello":
        # User types 'hello' or 'hallo'
        selected_text = random.choice(hello_answers)
    elif bool([element for element in Sentences.insults if(element in message)]):
        # User types any insults listed in Sentences.insults
        selected_text = random.choice(insult_answers)

    update.message.reply_text(selected_text)


def error(update, context):
    """Error message"""
    update.message.reply_text("ER-rohr")


def main():
    """ """

    dv.load_dotenv()
    token = os.getenv("TOKEN")

    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", start))

    dispatcher.add_handler((MessageHandler(Filters.text, msg_replys)))

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
