from pyrogram import filters
from bot.utils.ui import main_menu, back

def register(app):

    @app.on_callback_query()
    async def cb(_, q):
        data = q.data

        if data == "main_menu":
            await q.message.edit_text("Main Menu", reply_markup=main_menu())

        elif data == "plan_menu":
            await q.message.edit_text("Free Plan", reply_markup=back())

        elif data.startswith("quality_"):
            await q.message.edit_text("Starting download...", reply_markup=back())

        await q.answer()
