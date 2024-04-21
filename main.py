import logging

from telegram.ext import ApplicationBuilder, CommandHandler, Application

from bot.common.dispatch import dispatcher_init
from bot.handlers.start import start
from bot.settings import settings


def create_app() -> Application:
    logging.info("Create app")
    dispatcher_init()
    app = ApplicationBuilder().token(settings.bot_token).build()
    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)
    return app


if __name__ == '__main__':
    create_app().run_polling()
