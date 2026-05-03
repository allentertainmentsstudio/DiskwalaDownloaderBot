import os
import asyncio
import time
from bot.utils.downloader import download_file
from bot.utils.uploader import progress
from bot.utils.queue import active_tasks, user_tasks

DOWNLOAD_DIR = "downloads"


async def process_task(client, message, url, user_id):
    file_name = "video.mp4"
    path = os.path.join(DOWNLOAD_DIR, file_name)

    status = await message.reply_text("⏳ Starting download...")

    # DOWNLOAD
    file_path = await download_file(url, path, status, file_name)

    # UPLOAD
    start = time.time()

    await client.send_video(
        chat_id=message.chat.id,
        video=file_path,
        progress=progress,
        progress_args=(status, start, file_name)
    )

    # CLEANUP
    try:
        os.remove(file_path)
    except:
        pass

    user_tasks[user_id] = []
    active_tasks.pop(user_id, None)
