import asyncio

queue = asyncio.Queue()
active_tasks = {}
user_tasks = {}

MAX_GLOBAL = 10

async def worker():
    while True:
        user_id, coro = await queue.get()
        active_tasks[user_id] = coro
        try:
            await coro()
        except Exception as e:
            print(e)
        finally:
            active_tasks.pop(user_id, None)
            queue.task_done()

def start_workers(loop):
    for _ in range(MAX_GLOBAL):
        loop.create_task(worker())
