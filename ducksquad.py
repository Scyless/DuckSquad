'''
Created on Jun 27, 2019
Python version 3.5
@name: DuckSquad
@author: Scy
'''

import discord
from discord.ext.commands import Bot
from discord import Game
from discord.utils import get
import random
import re

# Backbone
BOT_PREFIX = ("!")
duck = Bot(command_prefix=BOT_PREFIX)
duck.remove_command('help')


# Shows avaiable commands
@duck.command()
async def quack():

    embed = discord.Embed(title="Seems like you quackes for help. Maybe there's still some hope left for you.", description="Note: This bot is not meant to be taken seriously. If you're offended by any jokes, that's on you.", color=0xff0000)

    embed.add_field(name="!ducks", value="Sends the best animal.", inline=False)
    embed.add_field(name="!shitpost", value="Sends bad jokes written by 'Mongokyou' or 'Lil Tupac' on Discord.", inline=False)
    embed.add_field(name="!rps", value="A rock paper scissors game. example: *!rps rock*, *!rps paper*", inline=False)
    embed.add_field(name="!gopnik", value="Sends various gopniks that represent you. No offense towards russians, I love their culture.", inline=False)
    embed.add_field(name="!hardbass", value="Sends hardbass via youtube links.", inline=False)
    embed.add_field(name="!spirit", value="Shows your real spirit animal. Idea and pictures by 'Mongokyou' or 'Lil Tupac' on Discord.", inline=False)
    embed.add_field(name="!ping", value="Pong.", inline=False)
    embed.add_field(name="!coinflip", value="Flips a coin. Idea by 'Mongokyou' or 'Lil Tupac' on Discord.", inline=False)
    embed.add_field(name="!anime", value="Recommends the one and only anime. Idea by 'Mongokyou' or 'Lil Tupac' on Discord.", inline=False)
    embed.add_field(name="!hug", value="Hugs the person you mention. Idea by 'Mongokyou' or 'Lil Tupac' on Discord. Example: *!hug @Scyless", inline=False)
    embed.add_field(name="!cat", value="Sends cat. Idea and pictures by 'Mongokyou' or 'Lil Tupac' on Discord.", inline=False)

    await duck.say(embed=embed)


@duck.command()
async def ducks():
    
    ducks = [
        'https://i.imgur.com/ROdcHRQ.jpg',
        'https://i.imgur.com/tfSWPwz.jpg',
        'https://i.imgur.com/A6DWZbO.jpg',
        'https://i.imgur.com/w7Ikq3z.jpg',        
        'https://i.imgur.com/3x6JtzK.jpg',
        'https://i.imgur.com/DvGSwL9.jpg',
        'https://i.imgur.com/4qKfQSo.jpg',      
        'https://i.imgur.com/ThmRffU.jpg',
        'https://i.imgur.com/9jjdACY.jpg',
        'https://i.imgur.com/we6HQa5.jpg',
        'https://i.imgur.com/h2IpsiA.jpg',
        'https://i.imgur.com/jeW6CoR.jpg',
        'https://i.imgur.com/DA4uTzW.jpg',
        'https://i.imgur.com/IC3wQBQ.png',
        'https://i.imgur.com/lQEvzDd.jpg',
        'https://i.imgur.com/DAX769L.jpg',
        'https://i.imgur.com/XUfIemU.jpg',
        'https://i.imgur.com/TRza346.jpg',
        'https://i.imgur.com/HkKklc8.jpg',
        'https://i.imgur.com/nSmDEri.jpg',
        'https://i.imgur.com/eQQ1qVz.jpg',
        'https://i.imgur.com/ZL4W44A.jpg',
        'https://i.imgur.com/nH6dqY9.png',
        'https://i.imgur.com/NtSgwt9.png',
        'https://i.imgur.com/Ib4hpXj.jpg',
        'https://i.imgur.com/JeisB23.png',
        'https://i.imgur.com/vc3QqS9.jpg',
        'https://i.imgur.com/KK2wcCu.jpg',
        'https://i.imgur.com/XjRZyng.jpg',
        'https://i.imgur.com/mHRmqfN.jpg',
        'https://i.imgur.com/8IG3TLQ.jpg',
        'https://i.imgur.com/NTpMqLO.jpg',
        'https://i.imgur.com/kE4QkRq.jpg',
        'https://i.imgur.com/0iKMdZS.jpg',
        'https://i.imgur.com/sE4dwLu.jpg'
        ]


    await duck.say(random.choice(ducks))

# Send puns
@duck.command()
async def shitpost():

    puns = [
    '''People cry, not because they\'re weak. 
    Its because they\'ve been strong for too long 
    - *Johnny Depp* 

    ||Thats kinda Johnny Deep||''',
    '''Pun more like Schimpunse''',
    '''Keanu Reeves last words

    ||"I'm intoxicating!"||''',
    '''You wanna hear a joke? Well, let me tell you one.
    
    ||**YOU!**||''',
    '''Why can't you get a girlfriend?

    ||**MAN'S NOT HOT!**||
    - *Big Shaq*''',
    '''My teacher asked me to choose a craft.

    ||I chose Minecraft!||'''
    ]

    await duck.say(random.choice(puns))
    
# Plays Rock Paper Scissors with you
@duck.command(pass_context=True)
async def rps(context):
    
    msg = (context.message.content)
    nmsg = re.sub('!rps ', '', msg) # Removes !rps from the decision
    happy = [
        ', eyo I won!',
        ', did you know that ducks are naturally smarter than humans?',
        ', can\'t beat a duck without luck.'
        ]
    sad = [
        ', beginners luck.',
        ', one more time, please?',
        ', even ducks can\'t be the best at everything.'
        ]
    neutral = [
        ', draw!',
        ', sounds like we have to try again. Don\'t blame me.',
        ', shmuck a duck, no winner.'
        ]
    gestures = [
    '**Rock**',
    '**Paper**',
    '**Scissors**'
                ]
     
    result = (random.choice(gestures)) 

# I'm sure there's an easier way. However, I was more comfortable using 'if' statements
    if 'rock' in nmsg and 'Rock' in result:
        await duck.say(result + random.choice(neutral))
    else:
        if 'scissor' in nmsg and 'Rock' in result:
            await duck.say(result + random.choice(happy))
        else:
            if 'paper' in nmsg and 'Rock' in result:
                await duck.say(result + random.choice(sad))
                return
            else:
                if 'rock' in nmsg and 'Scissor' in result:
                    await duck.say(result + random.choice(sad))
                else:
                    if 'scissor' in nmsg and 'Scissor' in result:
                        await duck.say(result + random.choice(neutral))
                    else:
                        if 'paper' in nmsg and 'Scissor' in result:
                            await duck.say(result + random.choice(happy))
                        else:
                            if 'rock' in nmsg and 'Paper' in result:
                                await duck.say(result + random.choice(happy))
                            else:
                                if 'paper' in nmsg and 'Paper' in result:
                                    await duck.say(result + random.choice(neutral))
                                else:
                                    if 'scissor' in nmsg and 'Paper' in result:
                                        await duck.say(result + random.choice(sad))
                                        return
     

# Sends 6 random gopniks    
@duck.command()
async def gopnik():
    
    gopniks = [
        'You are Zakhar. At least you\'re good at cooking, right? https://i.imgur.com/3evE7Je.png',
        'Vasya. Bold. Dangerous. Steals ducks. https://i.imgur.com/fjf3Sxk.png',
        'Don\'t smoke, kid. Evgeny, a smoker and vodka enthusiast. https://i.imgur.com/klYqakb.png',
        'The cool one, Artyom. For you, Heroes of Might and Magic is more important than women. Honestly, understandable. https://i.imgur.com/dNFqYDR.png',
        'Boris (Becker). You love tennis, vodka and men. https://i.imgur.com/G86oL15.png',
        'Dima. You listen to metal (good choice by the way) and own every Jacke Chan movie. My dream man. https://i.imgur.com/uie3u5r.png'
        ]
    
    await duck.say(random.choice(gopniks))


# Sends random predefined russian hardbass via youtube links    
@duck.command()
async def hardbass():
    songs = [
        'https://www.youtube.com/watch?v=BnTW6fZz-1E',
        'https://www.youtube.com/watch?v=V3hL0IEKbq4',
        'https://www.youtube.com/watch?v=fro6je9L5kg',
        'https://www.youtube.com/watch?v=QiFBgtgUtfw',
        'https://www.youtube.com/watch?v=ZJg-oiCMSt4',
        'https://www.youtube.com/watch?v=A1PAO3jgmXY',
        'https://www.youtube.com/watch?v=2tch4J_pP9o'
        ]
    await duck.say('GET OUT OF HERE, STALKER ' + random.choice(songs))
  
# Sends a random spirit animal
@duck.command()
async def spirit():
    spirit = [
        
        'Weak alone strong together! https://i.imgur.com/94GQR9r.jpg',
        'I\'ve got an idea. You\'re a batoidea https://i.imgur.com/LmUTspS.jpg',
        'Daddy material https://i.imgur.com/ywQKl37.jpg',
        'Hope your neck isn\'t the only large thing on your body https://i.imgur.com/7TvUQ1i.jpg',
        'He\'s aware of your dirty fantasies https://i.imgur.com/Uw1pnpU.jpg',
        'Rama Lama Ding Dong! https://i.imgur.com/3gBmagJ.jpg',
        'Born leader! https://i.imgur.com/ihUjzOl.jpg',
        'Everyone loves you https://i.imgur.com/tCZ5Ki1.jpg',
        'Sanic the Hegehog https://i.imgur.com/64W6TzA.png',
        'I feel sorry for you! https://i.imgur.com/7UbUIhS.jpg',
        'ARRRRRR you\'re a piRAT https://i.imgur.com/FNzoT5h.jpg',
        'Black or White I dont care https://i.imgur.com/IRyJ74O.jpg',
        'Eye of the Tiger! https://i.imgur.com/2VF2Tn2.jpg',
        'Shake your ass for the king https://i.imgur.com/MIwpd11.png',
        'Congratulation! You\'re a disabled bird https://i.imgur.com/wCoJYJv.jpg',
        'Let\'s build a wall! https://i.imgur.com/vpcuRWO.jpg',
        'Fat, cute and fluffy just like you! https://i.imgur.com/ElFO6vS.jpg',
        'Don\'t kill Nemo! https://i.imgur.com/dF6mbUN.jpg',
        'Lets hunt the ants https://i.imgur.com/lArlh1r.jpg',
        'Nice hair bro! https://i.imgur.com/lmhHHMh.jpg',
        'You\'ve got precious eyes https://i.imgur.com/0qZGxO7.jpg',
        'Stereotypical Gamer! https://i.imgur.com/nv8Rqnw.jpg',
        'Nyaaaaa! =o= https://i.imgur.com/C43nXtb.jpg',
        'There is no help for you! https://i.imgur.com/AuKfkxt.png',
        'The hat says Slytherin! https://i.imgur.com/qi03TPn.jpg',
        'Gotta go fast! https://i.imgur.com/EBjuXRj.jpg'
        ]

    await duck.say(random.choice(spirit))
    
# Pong.
@duck.command()
async def ping():
    
    await duck.say('Pong.')
    
# Why r u not smart? 
@duck.command()
async def pong():

    await duck.say('That\'s not how this works.')
    
# 50/50 chance coinflip
@duck.command(pass_context=True)
async def coinflip(context):

    choices = ['You got Tails!', 'You got Heads!']
    
    await duck.say(random.choice(choices))
    
# Sends a single link
@duck.command()
async def anime():
    
    await duck.say('You should watch Boku no Pico https://i.imgur.com/Yicm7Mo.jpg')


@duck.command(pass_context=True)
async def hug(context):
    
    links = [
        'https://i.imgur.com/GuADSLm.gif',
        'https://i.imgur.com/VgP2ONn.gif',
        'https://i.imgur.com/6CLb6BE.mp4',
        'https://i.imgur.com/bL9iuEI.gif',
        'https://i.imgur.com/RPYNm9o.gif',
        'https://i.imgur.com/KFZNUZl.gif',
        'https://i.imgur.com/HQmTIos.gif',
        'https://i.imgur.com/sjBLD2p.mp4',
        'https://i.imgur.com/QFU1X1p.gif',
        'https://i.imgur.com/ReFdPgW.gif',
        'https://i.imgur.com/V4n129V.gif'
        ]
    
    msg = (context.message.content)
    nmsg = re.sub('!hug ', '', msg) # Removes !hug from the decision
    
    hugs = [
        'Nobody deserves to be alone, not even ducks.',
        'Everyone needs a good hug once in a while',
        'Did you know that hugging {} actually has health benefits?'.format(nmsg),
        'Have you ever thought about hugging {}? Don\'t do it, pet him/her/it.'.format(nmsg),
        'K-On! has the most hug scenes. Go watch  it.',
        '{} hugs {}!'.format(context.message.author.mention, nmsg)
        ]


    await duck.say (random.choice(hugs) + ' ' + random.choice(links)) # Send random message with random gif


# Sends nekos
@duck.command()
async def cat():
    
    cats = [
        'https://i.imgur.com/Ndkt3Fp.jpg',
        'https://i.imgur.com/iKMsvO2.jpg',
        'https://i.imgur.com/wmlvNzL.jpg',
        'https://i.imgur.com/XlexY66.jpg',
        'https://i.imgur.com/7umKWKz.jpg',
        'https://i.imgur.com/XtvhBGK.jpg',
        'https://i.imgur.com/zPp1fHe.jpg',
        'https://i.imgur.com/3nhnGMS.jpg',
        'https://i.imgur.com/O1DFR9r.jpg',
        'https://i.imgur.com/5pAoMNP.jpg',
        'https://i.imgur.com/OuiBeSb.jpg',
        'https://i.imgur.com/OuiBeSb.jpg',
        'https://i.imgur.com/IrY3ePp.jpg',
        'https://i.imgur.com/IrY3ePp.jpg',
        'https://i.imgur.com/EFJdpok.jpg',
        'https://i.imgur.com/sanA2uk.jpg',
        'https://i.imgur.com/FvxToA9.jpg'
        ]
    
    await duck.say(random.choice(cats))
    

# Secret command
@duck.command()
async def barth():
    await duck.say('KENNSTE KENNSTE?? https://cps-static.rovicorp.com/3/JPG_400/MI0004/190/MI0004190678.jpg?partner=allrovi.com')

    
# Change 'playing', give ID in console and connect
@duck.event
async def on_ready():
    
        await duck.change_presence(game=Game(name='write !quack for help'))
        print('ID - ' + duck.user.id)
        print('Now connected. Let\'s hope I didn\'t mess anything up.')
        print('----------')

TOKEN = 'YourTokenHere'
duck.run(TOKEN)