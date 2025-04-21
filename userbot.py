from telethon import TelegramClient, events
from telethon.tl.types import KeyboardButton, ReplyKeyboardMarkup

# Replace these with your own values
api_id = '23097454'
api_hash = 'c244cdd380d02f0d51eca49df46db852'
phone_number = '+916232316832'  # phone number for your userbot

session_name = '1BVtsOH4BuyFVa_5MtezsbthBnIdGYxmbh15IpUZjB8aEIKqGW8txMz5voEJuHyN97tojL8ShAjGouq9b13bnmhMvoiq3iwz1mUWBA_kuLzs9dt7SX2Od_b6j8Rtc8055vnUqFuFhHB-lNYvzGCi6I6jjEh-kLrMiUr4H68gjnbmsWwDEi8XxnQPb_hlk7UpMxeDozcBR2lI7PFoi5TRazzXLqlzpvK0cffwSprwiotGco1ZLh_ciMH1gOdNfnfUJs52UldX0a2b8p2F4om7VV2p6z2IS1wm3D6bsDGf8w1EY_cbzSXnsUWkDUgxmG4mEBm-hvLRmTJOlz3NV0hewofUiymst61c='  # Modify as needed
client = TelegramClient(session_name, api_id, api_hash)

# Function to handle when the bot is added to a group
@client.on(events.ChatAction)
async def handler(event):
    if event.user_added:  # Check if the bot has been added to a group
        group = event.chat
        # Create custom reply keyboard
        keyboard = [
            [KeyboardButton('Button 1'), KeyboardButton('Button 2')],
            [KeyboardButton('Button 3')]
        ]
        markup = ReplyKeyboardMarkup(keyboard, resize=True)

        # Send a hidden message with the buttons (no visible text)
        await client.send_message(group, '', reply_markup=markup)  # Empty string ensures no visible message is sent
        print(f'Added to group: {group.title}')

# Start the client
client.start(phone_number)
client.run_until_disconnected()
