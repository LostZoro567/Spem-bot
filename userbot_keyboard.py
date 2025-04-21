from telethon import TelegramClient, events, Button

api_id = 23097454
api_hash = 'c244cdd380d02f0d51eca49df46db852'
session_name = 'userbot_session'

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.ChatAction)
async def on_chat_action(event):
    me = await client.get_me()
    for u in event.users:
        if u.id == me.id and (event.user_added or event.user_joined):
            keyboard = Button.keyboard(
                [['🔥 Hot Take', '❓ Ask a Question', '🎉 Celebrate!']],
                resize=True
            )
            await client.send_message(
                event.chat_id,
                'Choose an action below:',
                buttons=keyboard
            )
            break

# === New: /start command handler ===
@client.on(events.NewMessage(pattern=r'^/start$'))
async def start_command(event):
    keyboard = Button.keyboard(
        [['🔥 Hot Take', '❓ Ask a Question', '🎉 Celebrate!']],
        resize=True
    )
    await event.reply(
        'Welcome! Choose an action below:',
        buttons=keyboard
    )

if __name__ == '__main__':
    client.start()
    print('Userbot is up and running…')
    client.run_until_disconnected()
