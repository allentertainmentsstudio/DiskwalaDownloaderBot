from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """
✨ Welcome to Diskwala Video Downloader ✨

📥 Go to diskwala.com open a video click on share button copy the link and send it to me
I will download the full video in HD for you 🎬

✅ Supported link formats  
⚡ Fast • Reliable • Free  
🚀 Powered by @anujedits76

👇 Please send me your link
"""

START_BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("📥 Download Status", callback_data="download_status")],
    [
        InlineKeyboardButton("🚀 Plan", callback_data="plan_menu"),
        InlineKeyboardButton("📋 My Queue", callback_data="my_queue")
    ],
    [
        InlineKeyboardButton("🤝 Share Bot", callback_data="share_bot"),
        InlineKeyboardButton("💎 Premium", callback_data="premium_menu")
    ],
    [
        InlineKeyboardButton("ℹ️ About", callback_data="about_menu"),
        InlineKeyboardButton("❓ Help", callback_data="help_menu")
    ]
])
