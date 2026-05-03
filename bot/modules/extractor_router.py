from bot.modules.extractors.diskwala import extract

async def run_extractor(url):
    return await extract(url)
