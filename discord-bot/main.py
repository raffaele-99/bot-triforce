import discord
import os
import random
from dotenv import load_dotenv

intents = discord.Intents.all()


client = discord.Bot(intents = intents)
token = os.getenv('TOKEN')

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    the_word = "doing "
 
    if message.author == client.user:
        return

    print(f'Message {message.content} by {username} on {channel}')
 
    if the_word in user_message:
        begins = user_message.index(the_word) + 6
        ends = len(user_message)
        response = user_message[begins:ends]
        response = response.replace('my','your')
        await message.channel.send(f'I\'m {response}')
        return
    

client.run(token)