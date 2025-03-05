import os, asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from Abhi.Handlers import start, help_command, handle_message, newchat_command, init_chatgpt
from Abhi.Filters import AuthorizedUserFilter

def start_bot():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_chatgpt())
    app = Application.builder().token(os.getenv("BOT_TOKEN", "8095096286:AAGtId-d51HL7ezrDnqffKeQ4WF9ONEMieI")).build()
    
    # Commands
    app.add_handler(CommandHandler("start", start, filters=AuthorizedUserFilter()))
    app.add_handler(CommandHandler("help", help_command, filters=AuthorizedUserFilter()))
    app.add_handler(CommandHandler("new", newchat_command, filters=AuthorizedUserFilter()))
    
    # Messages
    app.add_handler(MessageHandler( AuthorizedUserFilter() & ~filters.COMMAND & filters.TEXT, handle_message))
    
    # Run the bot until the user presses Ctrl-C
    app.run_polling(allowed_updates=Update.ALL_TYPES)
