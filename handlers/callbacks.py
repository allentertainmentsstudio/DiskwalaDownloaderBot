from pyrogram import filters
from pyrogram.types import CallbackQuery
from bot.main import app

DOWNLOAD_READY = """
📥 Download Ready!

Ready to boom ! 😄  
Bhejo link, download kar dunga! 🚀

✅ Supported link formats
• Links containing /s/
• Links containing ?surl=

👇 Bas apna diskwala link paste karo!
"""


@app.on_callback_query()
async def callbacks(client, query: CallbackQuery):
    data = query.data

    if data == "download_status":
        await query.message.edit_text(DOWNLOAD_READY)

    elif data == "plan_menu":
        await query.message.edit_text("🚀 Your Plan: FREE")

    elif data == "my_queue":
        await query.message.edit_text("📋 Your queue is empty.")

    elif data == "share_bot":
        await query.message.edit_text("🤝 Share this bot!")

    elif data == "premium_menu":
        await query.message.edit_text("💎 Premium coming soon!")

    elif data == "about_menu":
        await query.message.edit_text("ℹ️ Diskwala Downloader Bot")

    elif data == "help_menu":
        await query.message.edit_text("❓ Send link to download.")

    await query.answer()
