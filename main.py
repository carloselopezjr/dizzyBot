# Each user interacts with the Discord backend to write and read messages
# Then, the Discord backend servers will broadcast an event to any program 
# listening that a new message has been posted
# Discord's API allows us to read and send messages to its backend servers

import discord
import os

class MyClient(discord.Client): # Represents connection to discord

    # async keyword allows the function to pause and resume as Discord events occur
    async def on_ready(self): 
        print("Logged on as {0}!".format(self.user))
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith("$hi"):
            await message.channel.send("hello")
        elif message.content.startswith("$lolskiii"):
            await message.channel.send("https://cdn.discordapp.com/attachments/1348050909162242120/1435368228158443610/IMG_4994.jpg?ex=690bb655&is=690a64d5&hm=b98fb3b50907d8f30662f4c742208d7ba57dcfb74306a2a01bdba4af9f068304&")

# Setting what our discord bot can access
intents = discord.Intents.default()
intents.message_content = True

# Create new instance of MyClient and starts client
client = MyClient(intents=intents)
client.run("") # my token hide before push
os.getenv()

