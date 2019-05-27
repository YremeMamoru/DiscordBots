import disLog
import discord
from discord.ext import commands

disLog.logActions()

TOKEN = 'Your token here'
'''
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------------')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith(';'): #== ';who':
            await message.channel.send("Eu sou o super mad scientist maluco, HOUOIN KYOUMA DA!")



'''
client = discord.Client()
'''
@bot.command()
async def square(number):
    squared_value = int(number) * int(number)
    await square.send(str(number) + " squared is " + str(squared_value))
'''

@client.event
async def on_message(message):
    channel = message.channel
    msg = message.content
    if message.author == client.user:
        return

    if msg.startswith(';square '):
        splitMsg = msg.split()
        number = float(splitMsg[1])
        squared = int(number*number)

        await channel.send(str(number) + " ao quadrado é " + str(squared))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')



#client = MyClient()
client.run(TOKEN)
