from telethon import TelegramClient, events, Button

api_id = 23097454
api_hash = 'c244cdd380d02f0d51eca49df46db852'
session_name = 'userbot_session'

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(outgoing=True, pattern=r'^\$start$'))
async def start_command(event):
    """
    Triggered whenever *you* type exactly "$start" in any chat.
    """
    # build the inline keyboard
    keyboard = Button.keyboard(
        [
            ['🔥 Hot Take', '❓ Ask a Question', '🎉 Celebrate!']
        ],
        resize=True
    )
    # reply in the same chat
    await event.respond('Choose an action below:', buttons=keyboard)

if __name__ == '__main__':
    client.start()
    print('Userbot is up and running…')
    client.run_until_disconnected()
