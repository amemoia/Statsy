import discord
import time
from modules import tools

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)
cogs = ['overwatch']

@bot.event
async def on_ready():
    print(" ")
    tools.console("Bot online!")
    tools.console(f"Username: {str(bot.user)}")
    tools.console(f"Currently in {len(bot.guilds)} guilds")
    print(" ")

@bot.slash_command(name = 'ping', description = "Check the bot's response time.")
async def ping(ctx):
    latency = round(bot.latency*1000)
    e = tools.embed(bot, title="🏓 Pong!", desc=f"This took me {latency}ms.")
    await ctx.respond(embed=e)

@bot.slash_command(name = 'invite', description = "Generate an invite link.")
async def invite(ctx):
    url = discord.utils.oauth_url(client_id=bot.user.id, permissions=discord.Permissions.advanced())
    e = tools.embed(bot, title="📨 Invite Link", desc=f"You can invite me using [this link]({url}).")
    await ctx.respond(embed=e)

for cog in cogs:
    bot.load_extension(f'cogs.{cog}')

bot.run(tools.token())
