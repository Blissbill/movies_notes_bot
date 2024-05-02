from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from bot.common.dispatch import Dispatcher
from bot.models.user import User
from bot.context import CustomContext
from telegram.constants import ParseMode

async def start(update: Update, context: CustomContext):
    user = User.query.filter_by(telegram_id=update.effective_user.id).first()
    if user is None:
        User.create(username=update.effective_user.username, telegram_id=update.effective_user.id,
                    first_name=update.effective_user.first_name, last_name=update.effective_user.last_name)
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=Dispatcher.messages.start)
    await update.message.reply_html(
        "This button was clicked <i>0</i> times.",
        reply_markup=InlineKeyboardMarkup.from_button(
            InlineKeyboardButton(text="Click me!", callback_data="button")
        ),
    )

async def count_click(update: Update, context: CustomContext) -> None:
    """Update the click count for the message."""
    context.message_clicks += 1
    await update.callback_query.answer()
    await update.effective_message.edit_text(
        f"This button was clicked <i>{context.message_clicks}</i> times.",
        reply_markup=InlineKeyboardMarkup.from_button(
            InlineKeyboardButton(text="Click me!", callback_data="button")
        ),
        parse_mode=ParseMode.HTML,
    )