from .core import AbstractTranslator
import discord

class DiscordClient(AbstractTranslator):
    name = "discord_client_post"

    def __init__(self, discord_channel_id, token):
        self.discord_channel_id = discord_channel_id
        self.token = token
    
    async def open(self):
        self.client = discord.Client(intents=discord.Intents.default())
        return [self.client.start(token=self.token)]

    def check(self):
        print('check')

    async def post(self, data):
        channel = await self.client.fetch_channel(self.discord_channel_id)
        await channel.send(data.text)
        print('post!')
    
    async def close(self):
        print('fin!')
        await self.client.close()
    