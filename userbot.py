from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
import time
from sqlite3 import OperationalError

api_id = 23097454
api_hash = "c244cdd380d02f0d51eca49df46db852"

# Manually insert the session string here
session_string = "BQFgcG4AC9uU8d9KK6b8meLQfgoJcZGxxXsWM9rMxIwmBzlG-ks2Wx6JtE6BikOJ35z3nPTRx9lXryT9AitO3_j2HqGGvQwFt0Gre6OMIP_vhO4mBTyhXPbcpkYItsgktv8ekW3QwQfS7HC5tkxMAFgm8Sn0M-hEQaJY1tj-mzKbJ_rrOOEWPASe6q7ZKEMB5HOIiCb9s_ndFilL8FI21uTt7g-uAEm0ZZ1OYN36qjxxpVwxS8Kw-oy0AhF3vqJppVUGXOQneEu26e-2mUhg7923N_mZTQhvjqmoGm7_89j-rxd24QP8Fftm5Cj01Oafcg0_zkA_rFz8_RYmhjM_sh_1q2tVEwAAAAHFDyhJAA"  # Replace this with your actual session string

app = Client(session_string, api_id=api_id, api_hash=api_hash)

keyboard = ReplyKeyboardMarkup(
    [["Hello"], ["Info"], ["Support"]],
    resize_keyboard=True,
    one_time_keyboard=False
)

# Function to safely load session and handle database lock
async def safe_connect():
    retries = 5
    while retries > 0:
        try:
            await app.start()
            print("[INFO] Successfully connected!")
            break
        except OperationalError as e:
            print(f"[ERROR] Database locked! Retrying... ({retries} retries left)")
            retries -= 1
            time.sleep(3)  # Wait before retrying
        except Exception as e:
            print(f"[ERROR] Error while connecting: {e}")
            break
    else:
        print("[ERROR] Failed to connect after multiple retries.")
        exit(1)

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

# Ensure session is loaded correctly before running the bot
app.run(safe_connect())  # Start the app after ensuring session is connected safely
