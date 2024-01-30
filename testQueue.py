import trio

from trio_queue.queue import Queue

async def main():
    async def consumer(q):
        while True:
            item = await q.get()
            print(f"Got {item}")
            q.task_done()
    
    async def producer(q):
        for i in range(10):
            await q.put(i)
            await trio.sleep(1)
        
    q = Queue()
    await q.put(1)
    
    async with trio.open_nursery() as nursery:
        nursery.start_soon(consumer, q)
        nursery.start_soon(producer, q)

    await q.join()
    print("Done")
    
if __name__ == "__main__":
    trio.run(main)