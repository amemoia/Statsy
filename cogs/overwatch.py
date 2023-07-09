import discord
from discord.ext import commands
from discord.commands import option, OptionChoice
import overfast

class Overwatch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def heroes(role: str = None):
        response = overfast.get(type='heroes', key=role)
        heroes = {}
        for hero in response:
            if not role:
                heroes[hero['key']] = hero['name']
            else:
                if hero['role'] == role:
                    heroes[hero['key']] = hero['name']
        return heroes
    
    def toChoices(inputs: dict):
        choices = []
        for key, display in inputs.items():
            a = OptionChoice(name=display.lower(), value=key)
            choices.append(a)
        return choices
    
    overwatch = discord.SlashCommandGroup('overwatch', 'Overwatch 2 related commands.')

    @overwatch.command(
        name = 'hero',
        description = 'fetch hero data'
    )
    @option(
        name = "name",
        description = "The name of the hero you want to look up.",
        required = True
    )
    async def hero(self, ctx, name: str):
        name = name.replace(' ', '-')
        # TODO notify user abt issue from exception Validation Error
        hero = overfast.get(type='hero', key=name)
        print(hero)
        await ctx.respond("check console")


def setup(bot):
    bot.add_cog(Overwatch(bot))