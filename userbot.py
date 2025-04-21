from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

api_id = 23097454     # replace with your api_id
api_hash = "c244cdd380d02f0d51eca49df46db852"

app = Client("user_session", api_id=..., api_hash=...)


keyboard = ReplyKeyboardMarkup(
    [["Hello"], ["Info"], ["Support"]],
    resize_keyboard=True,
    one_time_keyboard=False
)

@app.on_message(filters.new_chat_members)
async def send_keyboard(client, message):
    for member in message.new_chat_members:
        try:
            await message.reply(f"Welcome {member.first_name}", reply_markup=keyboard)
        except Exception as e:
            print(f"Error sending keyboard: {e}")

@app.on_message(filters.text & filters.reply)
async def handle_button(client, message):
    if message.text in ["Hello", "Info", "Support"]:
        await message.reply(message.text)

app.run()
