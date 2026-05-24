import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def sync_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # TODO: Route this to bot.core.engine
    await update.message.reply_text("🚀 DevFleetSync (Telegram): Syncing your domain...")

async def start_telegram(token):
    if not token:
        logging.warning("Telegram token missing. Skipping Telegram setup.")
        return

    # Build the application
    app = ApplicationBuilder().token(token).build()
    
    # Register the /sync command
    app.add_handler(CommandHandler("sync", sync_command))

    print("🟢 Telegram Adapter Online.")
    
    # Initialize and start polling asynchronously
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
