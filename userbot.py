from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
from pyrogram.sessions import StringSession

API_ID = 23097454
API_HASH = "c244cdd380d02f0d51eca49df46db852"
SESSION_STRING = "BQFgcG4AC9uU8d9KK6b8meLQfgoJcZGxxXsWM9rMxIwmBzlG-ks2Wx6JtE6BikOJ35z3nPTRx9lXryT9AitO3_j2HqGGvQwFt0Gre6OMIP_vhO4mBTyhXPbcpkYItsgktv8ekW3QwQfS7HC5tkxMAFgm8Sn0M-hEQaJY1tj-mzKbJ_rrOOEWPASe6q7ZKEMB5HOIiCb9s_ndFilL8FI21uTt7g-uAEm0ZZ1OYN36qjxxpVwxS8Kw-oy0AhF3vqJppVUGXOQneEu26e-2mUhg7923N_mZTQhvjqmoGm7_89j-rxd24QP8Fftm5Cj01Oafcg0_zkA_rFz8_RYmhjM_sh_1q2tVEwAAAAHFDyhJAA"

# Customize your buttons here
BUTTONS = {
    "https://t.me/Anime_Group_Chatting_Asia": "https://google.com",
    "@Anime_Group_Chatting_Asia": "https://github.com",
    "Join Anime Group": "https://youtube.com"
}

# Create reply keyboard layout
keyboard = ReplyKeyboardMarkup(
    keyboard=[[label] for label in BUTTONS],
    resize_keyboard=True,
    one_time_keyboard=False
)

# Set up client with string session
app = Client(
    session_name=StringSession(SESSION_STRING),
    api_id=API_ID,
    api_hash=API_HASH
)

# On any new member joining (even self), just send keyboard silently
@app.on_message(filters.new_chat_members)
async def on_join(client, message):
    if message.from_user and message.from_user.is_self:
        try:
            msg = await client.send_message(
                chat_id=message.chat.id,
                text=".",  # minimal invisible message
                reply_markup=keyboard,
                disable_notification=True
            )
            await client.delete_messages(message.chat.id, msg.id)
        except:
            pass  # fail silently

# Prevent bot from responding to any button press or text
@app.on_message(filters.text & ~filters.command(["alive", "$alive"]))
async def silence_buttons(client, message):
    pass

# Optional: $alive command (private chat only)
@app.on_message(filters.command(["alive", "$alive"]) & filters.private)
async def alive(client, message):
    await message.reply("✅ UserBot is alive and running!")

# Run the bot
app.run()
