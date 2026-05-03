from pyrogram import filters
from pyrogram.types import Message
from bot.main import app
from bot.start import START_TEXT, START_BUTTONS

active_tasks = {}
user_tasks = {}
TOTAL_DOWNLOADS = 10


def get_user_plan(user_id):
    return "FREE"


def get_user_queue_position(user_id):
    return 0


@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply_text(
        START_TEXT,
        reply_markup=START_BUTTONS
    )


@app.on_message(filters.command("stats"))
async def stats(client, message: Message):
    user_id = message.from_user.id

    text = f"""
📊 Bot Status Report

🤖 Bot ID: bot1
🔄 Global Active Tasks: {len(active_tasks)}/10

👤 Your Status:
🏷️ Plan: {get_user_plan(user_id)}
📥 Active Downloads: {len(user_tasks.get(user_id, []))}/1
📋 Queue: {get_user_queue_position(user_id)}
✅ Total Downloads: {TOTAL_DOWNLOADS}

💡 If your download is stuck, send /cancel to cancel all your tasks.
"""

    await message.reply_text(text)


@app.on_message(filters.command("cancel"))
async def cancel(client, message: Message):
    user_id = message.from_user.id

    if user_id not in user_tasks or not user_tasks[user_id]:
        return await message.reply_text("""
ℹ️ No Running Tasks Found

You currently have no active downloads on this bot
""")

    user_tasks[user_id] = []
    active_tasks.pop(user_id, None)

    await message.reply_text("✅ All downloads cancelled.")
