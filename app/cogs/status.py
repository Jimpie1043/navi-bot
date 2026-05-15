from discord.ext import commands


class Status(commands.Cog, name='Status'):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Status(bot))