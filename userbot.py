from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

API_ID = 23097454               # Replace with your API ID
API_HASH = "c244cdd380d02f0d51eca49df46db852" # Replace with your API Hash
SESSION_NAME = "BQFgcG4AC9uU8d9KK6b8meLQfgoJcZGxxXsWM9rMxIwmBzlG-ks2Wx6JtE6BikOJ35z3nPTRx9lXryT9AitO3_j2HqGGvQwFt0Gre6OMIP_vhO4mBTyhXPbcpkYItsgktv8ekW3QwQfS7HC5tkxMAFgm8Sn0M-hEQaJY1tj-mzKbJ_rrOOEWPASe6q7ZKEMB5HOIiCb9s_ndFilL8FI21uTt7g-uAEm0ZZ1OYN36qjxxpVwxS8Kw-oy0AhF3vqJppVUGXOQneEu26e-2mUhg7923N_mZTQhvjqmoGm7_89j-rxd24QP8Fftm5Cj01Oafcg0_zkA_rFz8_RYmhjM_sh_1q2tVEwAAAAHFDyhJAA"     # Will store session in this file

# Customize your buttons here
BUTTONS = {
    "Google": "https://google.com",
    "GitHub": "https://github.com",
    "YouTube": "https://youtube.com"
}

# Create reply keyboard layout
keyboard = ReplyKeyboardMarkup(
    keyboard=[[label] for label in BUTTONS],
    resize_keyboard=True,
    one_time_keyboard=False
)

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

# On any new member joining (even self), just send keyboard silently
@app.on_message(filters.new_chat_members)
async def on_join(client, message):
    # Only act if the userbot itself was added
    if message.from_user and message.from_user.is_self:
        try:
            await client.send_message(
                chat_id=message.chat.id,
                text=".",  # minimal invisible message
                reply_markup=keyboard,
                disable_notification=True
            )
            await client.delete_messages(message.chat.id, message.message_id + 1)
        except:
            pass  # fail silently (e.g. no permission)

# Prevent bot from responding to any button press or text
@app.on_message(filters.text & ~filters.command(["alive", "$alive"]))
async def silence_buttons(client, message):
    pass

# Optional: $alive command (only private chat)
@app.on_message(filters.command(["alive", "$alive"]) & filters.private)
async def alive(client, message):
    await message.reply("✅ UserBot is alive and running!")

app.run()
