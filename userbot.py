from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

api_id = 23097454
api_hash = "c244cdd380d02f0d51eca49df46db852"

app = Client("user_session", api_id=api_id, api_hash=api_hash)

keyboard = ReplyKeyboardMarkup(
    [["Hello"], ["Info"], ["Support"]],
    resize_keyboard=True,
    one_time_keyboard=False
)

@app.on_message(filters.new_chat_members)
async def send_keyboard(client, message):
    for member in message.new_chat_members:
        try:
            print(f"[INFO] New member joined: {member.first_name} ({member.id}) in group {message.chat.title}")
            await message.reply(
                f"Welcome {member.first_name}",
                reply_markup=keyboard
            )
        except Exception as e:
            print(f"[ERROR] Failed to send keyboard: {e}")

@app.on_message(filters.text & filters.reply)
async def handle_button(client, message):
    try:
        if message.text in ["Hello", "Info", "Support"]:
            print(f"[INFO] Button pressed: {message.text} from user {message.from_user.id} in chat {message.chat.id}")
            await message.reply(message.text)
    except Exception as e:
        print(f"[ERROR] Failed to handle button press: {e}")

@app.on_message(filters.command("alive", prefixes="$"))
async def alive_handler(client, message):
    try:
        print(f"[CHECK] $alive command received in chat {message.chat.id}")
        await message.reply("✅ Bot is alive and running!")
    except Exception as e:
        print(f"[ERROR] $alive check failed: {e}")

app.run()
