import random

import discord
from discord.ext import commands, tasks
from discord.ui import Button, View

import files_roles.roles_buttons as roles_buttons
from files_roles.Buttons import RolesButton

token_test = 'OTc4NDAyMTU2MTc4NzE0NzA1.GB7HAw.84DvES64T72_sEsnGl4eytYbNpY0xVAUBIYFZM'
token_main = 'OTc5MDc1NTU0OTMyMzEwMTc2.GUGZAw.q4_jsAIKlhpkJqszwZNYuTA4QAQ7vux8y1Ph9E'
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('ready')

@bot.command(name='roles', help='')
async def roles(ctx, *, message=''):

    msg = '''Добро пожаловать на наш сервер Toxic Family
Здесь ты можешь выбрать себе роли на сервере, чтобы настроить свой профиль и позволить всем пользователям сервера лучше узнать тебя.
Ты также сможешь выбирать роли, которые будут уведомлять тебя о новостях и событиях в игре и на сервере, чтобы ты ничего не пропустил !'''
    files = [discord.File(f'files_roles/roles.png')]
    message = await ctx.send(msg, files=files)

    for role in roles_buttons.all_list:
        view = View(timeout=365*24*60*60)
        msg = role[0]
        for i in role[2]:
            view.add_item(RolesButton(i, msg, role[1]))

        message = await ctx.send(msg, view=view)

bot.run(token_main)
