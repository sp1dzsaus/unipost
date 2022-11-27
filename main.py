from translators.discord import *
from translators.core import Address
import asyncio

import json

with open('config.json') as file:
    translator_data = json.load(file)["addresses"][0]


class Data:
    def __init__(self, text):
        self.text = text

data_test = Data('testing!')


async def test():
    print('test1')
    async with Address(translator_data) as trans:
        await asyncio.sleep(30)
        print('test2')
        await trans.post(data_test)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
tasks = [
    loop.create_task(test()),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

