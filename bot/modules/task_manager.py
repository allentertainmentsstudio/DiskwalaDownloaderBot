import os
import time

from bot.modules.downloader import download_file
from bot.modules.uploader import upload_progress
from bot.modules.extractor_router import extract
from bot.modules.queue_manager import active_tasks, user_tasks

DOWNLOAD_DIR = "downloads"


async def process_task(client, message, url, user_id):
    try:
        active_tasks[user_id] = True

        status_msg = await message.reply_text("🔍 Extracting video...")

        # STEP 1: Extract video URL
        data = await extract(url)

        if not data or not data.get("url"):
            return await status_msg.edit_text(
                "❌ Unable to fetch video\n🔒 This content may be protected or unsupported"
            )

        video_url = data["url"]
        file_name = data.get("title", "video.mp4")

        file_path = os.path.join(DOWNLOAD_DIR, file_name)

        # STEP 2: Download
        await status_msg.edit_text("📥 Starting download...")

        await download_file(
            video_url,
            file_path,
            status_msg,
            file_name
        )

        # STEP 3: Upload
        await status_msg.edit_text("📤 Uploading...")

        start_time = time.time()

        await client.send_video(
            chat_id=message.chat.id,
            video=file_path,
            caption=f"🎬 {file_name}\n⚠️ Auto delete after 1 hour",
            progress=upload_progress,
            progress_args=(status_msg, start_time, file_name)
        )

        # STEP 4: Cleanup
        try:
            os.remove(file_path)
        except:
            pass

        # Clear user state
        user_tasks[user_id] = []
        active_tasks.pop(user_id, None)

        await status_msg.delete()

    except Exception as e:
        active_tasks.pop(user_id, None)
        user_tasks[user_id] = []

        await message.reply_text(f"❌ Task failed: {str(e)}")    active_tasks.pop(user_id, None)
