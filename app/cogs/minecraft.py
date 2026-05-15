from discord.ext import commands


class Minecraft(commands.Cog, name='Minecraft'):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Minecraft(bot))