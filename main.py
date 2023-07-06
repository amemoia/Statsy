import discord
import overfast
import time
from modules import tools

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)
cogs = ['overwatch']

def console_print(msg: str, msg_type = None):
    if not msg_type:
        c = "#"
    if msg_type == "warn":
        c= "!"
    print(f"{tools.timestamp()}    {c}{c}{c}    {msg}")

@bot.event
async def on_ready():
    print(" ")
    console_print("Bot online!")
    console_print(f"Username: {str(bot.user)}")
    console_print(f"Currently in {len(bot.guilds)} guilds")
    print(" ")

@bot.slash_command(name = 'ping', description = "Check the bot's response time.")
async def ping(ctx):
    channel = ctx.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    latency = round((t2-t1)*1000)
    await tools.embed(bot, ctx, "🏓 Pong!", f"This took me {latency}ms.")

@bot.slash_command(name = 'invite', description = "Generate an invite link.")
async def invite(ctx):
    url = discord.utils.oauth_url(client_id=bot.user.id, permissions=discord.Permissions.advanced())
    await tools.embed(bot, ctx, "📨 Invite Link", f"You can invite me using [this link]({url}).")

for cog in cogs:
    bot.load_extension(f'cogs.{cog}')

bot.run(tools.token())
