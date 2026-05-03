from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Plan", "plan_menu"),
         InlineKeyboardButton("📋 My Queue", "my_queue")],
        [InlineKeyboardButton("🤝 Share Bot", "share_bot"),
         InlineKeyboardButton("💎 Premium", "premium_menu")],
        [InlineKeyboardButton("📥 Download Status", "download_status")],
        [InlineKeyboardButton("ℹ️ About", "about_menu"),
         InlineKeyboardButton("❓ Help", "help_menu")]
    ])

def quality_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("360p", "quality_360"),
         InlineKeyboardButton("480p", "quality_480")],
        [InlineKeyboardButton("720p", "quality_720"),
         InlineKeyboardButton("1080p", "quality_1080")],
        [InlineKeyboardButton("⬅ Back", "main_menu")]
    ])

def back():
    return InlineKeyboardMarkup([[InlineKeyboardButton("⬅ Back", "main_menu")]])
