from typing import Optional
import discord
from discord.ext import commands
import discord.ui
import os 

Token = ""

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.',intents=intents)



@bot.event
async def on_ready():
    print("bot start")
    bot.add_view(Verify())
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("hmm"))

class Verify(discord.ui.View):
        def __init__(self):
         super().__init__(timeout = None)    
        @discord.ui.button(label="verify", custom_id="รับยศ",style=discord.ButtonStyle.success)
        async def verify(self, interaction, button):
            await interaction.response.defer()
            user = interaction.user
            role = 1172498503159783475
            if role not in [y.id for y in user.roles
                            ]:
             await user.add_roles(user.guild.get_role(role))
             await user.send("คุณได้รับยศแล้ว")
             

@bot.command()
async def init(ctx):
    embed = discord.Embed(title= "รับยศ" , description= "click below to verify")
    await ctx.send(embed = embed, view = Verify())
        
   
bot.run(Token)