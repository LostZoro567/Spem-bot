from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

api_id = 23097454     # replace with your api_id
api_hash = "c244cdd380d02f0d51eca49df46db852"

app = Client("BQFgcG4AC9uU8d9KK6b8meLQfgoJcZGxxXsWM9rMxIwmBzlG-ks2Wx6JtE6BikOJ35z3nPTRx9lXryT9AitO3_j2HqGGvQwFt0Gre6OMIP_vhO4mBTyhXPbcpkYItsgktv8ekW3QwQfS7HC5tkxMAFgm8Sn0M-hEQaJY1tj-mzKbJ_rrOOEWPASe6q7ZKEMB5HOIiCb9s_ndFilL8FI21uTt7g-uAEm0ZZ1OYN36qjxxpVwxS8Kw-oy0AhF3vqJppVUGXOQneEu26e-2mUhg7923N_mZTQhvjqmoGm7_89j-rxd24QP8Fftm5Cj01Oafcg0_zkA_rFz8_RYmhjM_sh_1q2tVEwAAAAHFDyhJAA", api_id=api_id, api_hash=api_hash)

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
