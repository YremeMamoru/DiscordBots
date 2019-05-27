import disLog
import discord

disLog.logActions()

TOKEN = 'ur shit'

client = discord.Client()

@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return

    if message.content == ';hello':
        msg = 'Hello {0.author.mention}'.format(message)
        await channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')

client.run(TOKEN)
