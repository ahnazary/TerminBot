import telegram
from telegram.ext import CommandHandler, Updater

# Replace YOUR_BOT_TOKEN with the API key for your bot
updater = Updater(token="bot token", use_context=True)


def startup_function(update, context):
    # Send a message to the chat
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, World!")


startup_handler = CommandHandler("start", startup_function)
updater.dispatcher.add_handler(startup_handler)

# Start the bot
updater.start_polling()
