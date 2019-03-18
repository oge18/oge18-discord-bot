import discord
import random
import time
token = "NTU2OTg5MTAxNzY1Njg5MzQ0.D3ByPg.ccxefFhyvQC311EL5CSEmZUIu6s"
fopen = open('randword.txt').read().splitlines()
print('Loading')


client = discord.Client()
@client.event
async def on_ready(): 
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
        if "hi" in message.content.lower():
            await message.channel.send('Hello, I am the All Mighty Gamer\'s bot, nerd.')

        elif "rng10" in message.content.lower():
            rng = random.randint(1,10)
            await message.channel.send('Your random number between 1 & 10 is ' + str(rng))


        elif "rng100" in message.content.lower():
            rng = random.randint(1,100)
            await message.channel.send('Your random number between 1 & 100 is ' + str(rng))


        elif "coin flip" in message.content.lower():
            x = 1
            rng = random.randint(1,2)
            print(rng)
            if x == 1:
                await message.channel.send('The coin landed on *suspensfull drum roll*')
                time.sleep(1)
                await message.channel.send('.')
                time.sleep(1)
                await message.channel.send('.')
                time.sleep(1)
                await message.channel.send('.')
                time.sleep(1)
                if rng == 2:
                    file = discord.File("heads.jpg", filename="heads.jpg")
                    await message.channel.send('', file=file)
                elif rng == 1:
                    file = discord.File("tails.jpg", filename="tails.jpg")
                    await message.channel.send('', file=file)


        elif "rwg" in message.content.lower():
            word1 = random.choice(fopen)          
            await message.channel.send('Your random word is ' + word1)

        elif "rsg" in message.content.lower():
            word1 = random.choice(fopen)
            word2 = random.choice(fopen)
            word3 = random.choice(fopen)
            word4 = random.choice(fopen)
            await message.channel.send('Your random sentence is:')
            await message.channel.send(word1 + ' ' + word2 + ' ' + word3 + ' ' + word4)
                


client.run(token)

