from telethon import TelegramClient, events, Button

api_id = 123456
api_hash = 'your_api_hash_here'
session_name = ''userbot_session''

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.ChatAction)
async def on_chat_action(event):
    me = await client.get_me()
    if (event.user_added or event.user_joined) and event.user_id == me.id:
        keyboard = Button.keyboard(
            [['🔥 Hot Take', '❓ Ask a Question', '🎉 Celebrate!']],
            resize=True
        )
        await client.send_message(
            event.chat_id,
            'Choose an action below:',
            buttons=keyboard
        )

if __name__ == '__main__':
    client.start()
    print('Userbot is up and running…')
    client.run_until_disconnected()
