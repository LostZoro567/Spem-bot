from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Replace with your bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Button label to link mapping
BUTTON_LINKS = {
    "Google": "https://www.google.com",
    "YouTube": "https://www.youtube.com",
    "GitHub": "https://github.com"
}

# Handler for /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[label] for label in BUTTON_LINKS.keys()]  # one button per row
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Choose an option to get the link:", reply_markup=reply_markup)

# Handler for button press
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    if user_text in BUTTON_LINKS:
        await update.message.reply_text(f"Here is your link: {BUTTON_LINKS[user_text]}")
    else:
        await update.message.reply_text("Please use the buttons below.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()
