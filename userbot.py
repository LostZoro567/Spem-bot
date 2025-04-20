from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Define your button labels and their corresponding links
LINKS = {
    "@veggie_me Randi Behen K Lode": "@veggie_me ki gand mai danda dalo sab",
    "@veggie_me Chaddi Chor": "@veggie_me lund k tope",
    "@veggie_me Chutiya Kamina": "@veggie_me randi k"
}

# Set up the reply keyboard
keyboard = ReplyKeyboardMarkup(
    keyboard=[[button] for button in LINKS.keys()],
    resize_keyboard=True,
    one_time_keyboard=False
)

# $alive command handler
async def alive(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is alive and running!")

# Message handler for button presses
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in LINKS:
        await update.message.reply_text(f"Sale : {LINKS[text]}")

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! Tap a button to get the link.",
        reply_markup=keyboard
    )

# Synchronous startup
def main():
    app = ApplicationBuilder().token("7719887246:AAFPqDaDMEZMi3koh_kDIIabZLdAxx5-9M0").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("alive", alive))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running quietly... awaiting interaction.")
    app.run_polling()

if __name__ == "__main__":
    main()
