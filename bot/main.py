from pyrogram import Client
from bot.config import API_ID, API_HASH, BOT_TOKEN
from bot.handlers import commands, messages, callbacks

app = Client(
    "diskwala_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

commands.register(app)
messages.register(app)
callbacks.register(app)

if __name__ == "__main__":
    print("Bot running...")
    app.run()
