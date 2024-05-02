import logging

from telegram.ext import ApplicationBuilder, CommandHandler, Application, ContextTypes, CallbackQueryHandler

from bot.common.dispatch import dispatcher_init
from bot.context import CustomContext, ChatData
from bot.handlers.start import start, count_click
from bot.settings import settings


def create_app() -> Application:
    logging.info("Create app")
    dispatcher_init()
    app = ApplicationBuilder().token(settings.bot_token).context_types(ContextTypes(context=CustomContext, chat_data=ChatData)).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(count_click))
    return app


if __name__ == '__main__':
    create_app().run_polling()
