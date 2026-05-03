from pyrogram import filters
from bot.utils.ui import main_menu
from bot.modules.plans import get

def register(app):

    @app.on_message(filters.command("start"))
    async def start(_, m):
        await m.reply("👋 Welcome", reply_markup=main_menu())

    @app.on_message(filters.command("plan"))
    async def plan(_, m):
        await m.reply(f"Your plan: {get(m.from_user.id)}")

    @app.on_message(filters.command("cancel"))
    async def cancel(_, m):
        await m.reply("Cancelled")
