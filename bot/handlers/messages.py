from pyrogram import filters
from bot.main import app
from bot.utils.queue import add_task
from bot.modules.task_manager import process_task


@app.on_message(filters.text & ~filters.command(["start", "help"]))
async def link_handler(client, message):
    user_id = message.from_user.id
    text = message.text

    if "diskwala.com" not in text:
        return await message.reply_text("❌ Invalid link")

    task = {
        "func": process_task,
        "args": (client, message, text, user_id)
    }

    status = await add_task(user_id, task)

    if status == "queued":
        await message.reply_text("📋 Added to queue")
    else:
        await process_task(client, message, text, user_id)
