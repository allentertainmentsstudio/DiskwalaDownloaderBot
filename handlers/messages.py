from pyrogram import filters
from bot.utils.ui import quality_menu

def register(app):

    @app.on_message(filters.text)
    async def msg(_, m):
        if "diskwala" in m.text:
            await m.reply("Select Quality", reply_markup=quality_menu())
        else:
            await m.reply("Invalid link")
