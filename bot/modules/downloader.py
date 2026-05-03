import aiohttp, time
from bot.utils.progress import bar

async def download(url, path, msg):
    start = time.time()

    async with aiohttp.ClientSession() as s:
        async with s.get(url) as r:
            total = int(r.headers.get("content-length", 0))
            done = 0

            with open(path, "wb") as f:
                async for chunk in r.content.iter_chunked(1024):
                    f.write(chunk)
                    done += len(chunk)

                    percent = done*100/total if total else 0
                    speed = done/(time.time()-start+1)
                    eta = (total-done)/speed if speed else 0

                    await msg.edit_text(
                        f"📥 Downloading\n{bar(percent)} {percent:.1f}%\n"
                        f"{speed/1024:.1f} KB/s | ETA {eta:.1f}s"
                    )
