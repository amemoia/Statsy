import discord
from discord.ext import commands
import overfast

class Overwatch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def hero(self, ctx, hero):
        #
        data = overfast.get(type="hero", key=hero)
        print(data)
        
def setup(bot):
    bot.add_cog(Overwatch(bot))