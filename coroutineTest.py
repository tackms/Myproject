#encoding=utf-8


import asyncio
import requests
import time
import aiohttp

start = time.time()

async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.text()
    await session.close()
    return result

async def request():
    url = 'http://127.0.0.1:5000/'
    print('Waiting for',url)
    result = await get(url)
    print('get reponse from',url,'Result',result)

task = [asyncio.ensure_future(request()) for _ in range(500)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task))

end = time.time()

print('Cose :',end - start)


