from discord.ext import commands


class Logging(commands.Cog, name='Logging'):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Logging(bot))