from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

api_id = 23097454        # Replace with your API ID
api_hash = "c244cdd380d02f0d51eca49df46db852"  # Replace with your API Hash
session_string = "BQFgcG4AC9uU8d9KK6b8meLQfgoJcZGxxXsWM9rMxIwmBzlG-ks2Wx6JtE6BikOJ35z3nPTRx9lXryT9AitO3_j2HqGGvQwFt0Gre6OMIP_vhO4mBTyhXPbcpkYItsgktv8ekW3QwQfS7HC5tkxMAFgm8Sn0M-hEQaJY1tj-mzKbJ_rrOOEWPASe6q7ZKEMB5HOIiCb9s_ndFilL8FI21uTt7g-uAEm0ZZ1OYN36qjxxpVwxS8Kw-oy0AhF3vqJppVUGXOQneEu26e-2mUhg7923N_mZTQhvjqmoGm7_89j-rxd24QP8Fftm5Cj01Oafcg0_zkA_rFz8_RYmhjM_sh_1q2tVEwAAAAHFDyhJAA"  # Paste the session string here

app = Client(
    name="userbot",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session_string
)

@app.on_message(filters.new_chat_members)
async def welcome_buttons(client, message):
    me = await client.get_me()
    for new_member in message.new_chat_members:
        if new_member.id == me.id:
            # Create reply keyboard
            keyboard = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton("Button 1"), KeyboardButton("Button 2")],
                    [KeyboardButton("Button 3")]
                ],
                resize_keyboard=True
            )
            # Send only keyboard with no text
            await message.reply_text("", reply_markup=keyboard)

app.run()
