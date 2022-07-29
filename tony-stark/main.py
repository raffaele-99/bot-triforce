from asyncio import sleep
import discord
import os
import random
from dotenv import load_dotenv

# intents = discord.Intents.all()


client = discord.Bot()
token = os.getenv('TOKEN')

@client.event
async def on_message(message):
    id = message.author.id
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    c_channel = message.channel
    print(c_channel)
    messages = await c_channel.history(limit=2).flatten()
    id2 = messages[1].author.id
    print(id2)

    
    print(f'Message {message.content} by {username} on {channel}')

    if username == 'MJ Bot':
        await sleep(2)
        await message.channel.send(f'*laughing* <@{id2}>, your girlfriend is awesome!')
    

client.run(token)