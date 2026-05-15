from discord.ext import commands


class Setup(commands.Cog, name='Setup'):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Setup(bot))