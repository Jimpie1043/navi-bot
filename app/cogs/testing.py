from discord.ext import commands


class Testing(commands.Cog, name='Testing'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test', brief='For... Testing?', description='Replies with "test". Useful for checking bot status quickly.')
    async def test(self, ctx):
        await ctx.send('test')

    @commands.command(name='ping', brief='Returns bot latency.')
    async def ping(self, ctx):
        await ctx.send(f'Pong! ** {round(self.bot.latency*1000)}ms**')

async def setup(bot):
    await bot.add_cog(Testing(bot))