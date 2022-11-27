import asyncio

TRANSLATORS = {}

class AbstractTranslator():
    def __init_subclass__(cls):
        TRANSLATORS[cls.name] = cls

    def __init__(self, args):
        pass

    async def open(self):
        pass
    
    async def close(self):
        pass

    async def post(self, data):
        pass

class Address:
    def __init__(self, builder_args):
        self.translator = TRANSLATORS[builder_args["type"]](**builder_args["args"])

    async def __aenter__(self):
        runner = await self.translator.open()
        async def task():
            for run in runner:
                await run
        asyncio.create_task(task())
        return self.translator
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_tb, exc_val)
        await self.translator.close()
