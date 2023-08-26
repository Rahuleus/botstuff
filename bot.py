import discord
import requests
import json
import random
 
intents = discord.Intents().all()
client = discord.Client(intents=intents)
 
 
#first event :logging in
@client.event
async def on_ready():
  print("successful login as {0.user}".format(client))
 
 
#second event: sending message
@client.event
async def on_message(message):
  #check who sent the message
  if message.author == client.user:
    return
  msg = message.content
  if msg.startswith('hello'):
    await message.channel.send("hello!")
 
 
#getting the secret token
f = open("demofile", "r")
n=(f.read())
a=""
for i in range(len(n)-2):
    a += n[i]
client.run(a)
