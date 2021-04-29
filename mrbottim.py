import os
import dotenv as dv
import random

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
    update.message.reply_text("Booting up my booty.")

def help(update, context):
    update.message.reply_text("Bei dir ist jegliche Hilfe verloren.")

def hello(update, context):
    """ """
    answers = ["Du stinkst hart nach Maggi.", "Fettsack geh sport machen!", "Hier könnte ihr Werbung stehen",
               "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "MACH DAS SAUBER!", "Ein Baum hat mehr IQ als du.",
               "Waschlappen.", "Ich habe kein Fett bestellt.", "Du Null.", "Du CDU Wähler."
               "Ich hoffe deine Eltern versaufen das Kindergeld.", "Du Windows User."]

    if update.message.text.lower() == "hallo":
        selected_text = random.choice(answers)
        update.message.reply_text(selected_text)

def error(update, context):
    update.message.reply_text("ER-rohr")


def main():
    """ """

    dv.load_dotenv()
    token = os.getenv("TOKEN")

    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", start))

    dispatcher.add_handler((MessageHandler(Filters.text, hello)))

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
