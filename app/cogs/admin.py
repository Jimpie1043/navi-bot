from discord.ext import commands


class Admin(commands.Cog, name='Admin'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def admin(self, ctx):
        """Checks if the user is an admin."""
        msg = "You're an admin {}".format(ctx.message.author.mention)  
        await ctx.send(msg)

async def setup(bot):
    await bot.add_cog(Admin(bot))