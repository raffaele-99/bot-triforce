from asyncio import sleep
import discord
import os
import random
from dotenv import load_dotenv


client = discord.Bot()
token = os.getenv('TOKEN')

messageList = ['I shot my wife',
'BEST BY 07 SEP 18 043 | 49',
'When you\'re on iMessage go to the stickers on the bottom of the screen go to more on the right hand side click on more go to more apps in iMessage',
'does anyone wanna pony town date',
'It\'s a Dangerous Day to be a Berry 😈',
'My dog was diagnosed with terminal cancer',
'I owe four thousand nine hundred and five dollars to an advertising firm',
'I have been diagnosed with schizophrenia',
'The body is buried at -33.7748018 151.1155466',
'Sometimes, I still hear the screams',
'ｓｏｏｎ',
'They put something in my water to make me forget',
'this song feels like i did an epic backflip in front of markiplier but failed and got paralyzed from the waistdown causing me to shit myself.markiplier takes me to the hospital and he holds my hand and tells meeverything is gonna be ok but then the cyst in my brain explodes and causes me to flatline (they didnt knowabout the brain cyst until after the autopsy). markiplier falls to his knees and sobs uncontrollably until thenurses tell him to leave. He realizes theres nothing he can do anymore so he goes home and starts making avideo. he uploads a new fnaf video later that day but it has a different intro than usual. the video startscompletely silent on a black screen until it slowly fades to a picture of me in my hospital bed then transitionsto an image of very upset sad crying emoji emoticon stock vector that slowly zooms in. the video suddenlycuts back to normal with no context given. fans are left baffled.']

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    
    print(f'Message {message.content} by {username} on {channel}')

    if username == 'Tony Stark':
        await sleep(2)
        await message.channel.send(random.choice(messageList))
    

client.run(token)