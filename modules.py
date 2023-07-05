import os
import dotenv
import discord
from datetime import datetime

class Tools():
    def token(self):
        """Either returns a bot's token from .env or creates the file."""
        if not os.path.isfile('.env'):
            content = "TOKEN="
            ans = input("Please paste your bot's token and hit enter. \n")
            with open('.env', 'w') as env:
                env.write(content+ans)
        with open('.env', "r+") as env:
            dotenv.load_dotenv()
            return str(os.getenv("TOKEN"))
    
    def timestamp(self):
        """Returns a pre-formatted timestamp."""
        dt = datetime.now()
        ts = dt.strftime("%H:%M:%S")
        return ts

    async def embed(self, bot, ctx, title: str, desc: str, color: str = "normal"):
        colors = {
            "normal" : discord.Color.orange(),
            "warn": discord.Color.red()
        }
        ts = datetime.utcnow()
        embed = discord.Embed(title=title, description=desc, color=colors[color], timestamp=ts)
        embed.set_footer(icon_url=bot.user.avatar.url, text=bot.user.display_name)
        return await ctx.respond(embed=embed)

tools = Tools()