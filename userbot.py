from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

API_ID = 12345678               # Replace with your API ID
API_HASH = "your_api_hash_here" # Replace with your API Hash
SESSION_NAME = "my_session"     # Will store session in this file

# Define buttons and links
LINKS = {
    "Google": "https://google.com",
    "GitHub": "https://github.com",
    "YouTube": "https://youtube.com"
}

keyboard = ReplyKeyboardMarkup(
    keyboard=[[key] for key in LINKS.keys()],
    resize_keyboard=True,
    one_time_keyboard=False
)

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

# Show keyboard on /start or $start
@app.on_message(filters.command(["start", "Start", "$start"]))
async def start(client, message):
    await message.reply("Welcome! Tap a button to get a link.", reply_markup=keyboard)

# $alive check
@app.on_message(filters.command(["alive", "$alive"]))
async def alive(client, message):
    await message.reply("✅ UserBot is alive and running!")

# Send link when user taps a button
@app.on_message(filters.text & ~filters.command(["start", "alive"]))
async def send_link(client, message):
    if message.text in LINKS:
        await message.reply(f"Here is your link: {LINKS[message.text]}")

app.run()
