import warnings

warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    module="telegram.utils.request"
)

import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

# Create updater and dispatcher
updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define /start command handler
def start(update, context):
    update.message.reply_text("Hello! Bot is ready for working  🚀")

def help_command(update, context):
    """Handler for /help command"""
    update.message.reply_text("Hi there! I am telegram bot create by Rajib Saha to demonstrate basic functionality. You can use the following commands:\n\n/start - Start the bot\n/help - Show this help message\nJust send any text message and I will echo it back to you!")

def echo(update, context):
    """Echoes any text message sent by user"""
    text = update.message.text
    update.message.reply_text(f"You said: {text}")

# Add handler to dispatcher
def run_bot():
    # Create updater and dispatcher
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
    dispatcher.add_handler(telegram.ext.CommandHandler("help", help_command))
    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, echo))

    # Start the bot
    updater.start_polling()
    print("Bot is running...")
    updater.idle()

# Run bot if this file is executed
if __name__ == "__main__":
    run_bot()

