import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='monke ')
owner_id = 632339835658436648

@bot.event
async def on_ready():
    print('Logged in')
@bot.command()
async def kill(ctx, arg):  
    kill_messages = [
        f'{ctx.message.author.mention} stabbed {arg} with the legendary weapon, Banana Blade.', 
        f'{arg} was hit by a meteor shower of bananas.',
        f'{arg} tried to challenge {ctx.message.author.mention}. May they rest in peace.',
        f'{arg} played Fortnite.',
        f'{arg} hated monkes, so the monke gang took care of them.',
        f'{arg} choked on air and died.',
        f'{arg} looked at a mirror and had ai know stroke.',
        f'While mining, {arg} found some diamonds and was too distracted to notice the creeper behind them.',
        f'**"I, AM, INEVITABLE!!"** screamed {ctx.message.author.mention}, while {arg} faded into nothingness.'
    ]
    await ctx.send(random.choice(kill_messages))

@bot.command()
async def say(ctx,*,arg):
    await ctx.send(arg)


bot.run('token')
