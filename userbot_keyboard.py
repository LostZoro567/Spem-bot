from telethon import TelegramClient, events, Button

api_id = 23097454
api_hash = 'c244cdd380d02f0d51eca49df46db852'
session_name = 'userbot_session'

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(pattern=r'^\$start$'))
async def start_command(event):
    """
    When someone types exactly "$start" (case‑sensitive),
    send back the menu keyboard.
    """
    # Build your keyboard
    keyboard = Button.keyboard(
        [
            ['🔥 Hot Take', '❓ Ask a Question', '🎉 Celebrate!']
        ],
        resize=True
    )

    # You can use event.respond() to automatically reply to the same chat
    await event.respond(
        'Choose an action below:',
        buttons=keyboard
    )

if __name__ == '__main__':
    client.start()
    print('Userbot is up and running…')
    client.run_until_disconnected()
