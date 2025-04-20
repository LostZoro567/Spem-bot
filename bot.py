from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Define your button labels and their corresponding links
LINKS = {
    "Google": "https://google.com",
    "GitHub": "https://github.com",
    "YouTube": "https://youtube.com"
}

# Set up the reply keyboard (in case we send it later)
keyboard = ReplyKeyboardMarkup(
    keyboard=[[button] for button in LINKS.keys()],
    resize_keyboard=True,
    one_time_keyboard=False
)

# $alive command handler to check if the bot is running
async def alive(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is alive and running!")

# Message handler to respond to button presses
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in LINKS:
        await update.message.reply_text(f"Here is your link: {LINKS[text]}")

# Start command handler (this is for when the user directly sends /start)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Send the reply keyboard only when the user sends /start or a specific command.
    await update.message.reply_text(
        "Welcome! Tap a button to get the link.",
        reply_markup=keyboard
    )

# Bot setup
async def main():
    # Replace 'YOUR_BOT_TOKEN' with your BotFather token
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))  # /start command
    app.add_handler(CommandHandler("alive", alive))  # $alive command
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # Handle button presses

    print("Bot is running quietly... awaiting interaction.")
    await app.run_polling()

# Run the bot
import asyncio
asyncio.run(main())
