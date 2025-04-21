from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import KeyboardButton, ReplyKeyboardMarkup

api_id = 23097454      # Replace with your API ID
api_hash = 'c244cdd380d02f0d51eca49df46db852'  # Replace with your API hash

# This will keep session in memory (not saved to disk)
client = TelegramClient(StringSession(), api_id, api_hash)

@client.on(events.ChatAction)
async def on_added(event):
    # Trigger only when this user is added to a group
    if event.user_added and event.user_id == (await client.get_me()).id:
        keyboard = [
            [KeyboardButton('Button 1'), KeyboardButton('Button 2')],
            [KeyboardButton('Button 3')]
        ]
        markup = ReplyKeyboardMarkup(keyboard=keyboard, resize=True)
        
        # Send a hidden message with just keyboard
        await client.send_message(event.chat_id, '', reply_markup=markup)

# Start the client (will ask for login code if not logged in)
async def main():
    await client.start()
    print("Userbot is running...")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())
