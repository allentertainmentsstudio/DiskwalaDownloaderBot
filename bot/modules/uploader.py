import time
from bot.utils.progress import bar

async def progress(current, total, msg, start):
    p = current*100/total
    speed = current/(time.time()-start+1)
    eta = (total-current)/speed if speed else 0

    await msg.edit_text(
        f"📤 Uploading\n{bar(p)} {p:.1f}%\n"
        f"{speed/1024:.1f} KB/s | ETA {eta:.1f}s"
    )
