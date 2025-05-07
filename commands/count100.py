from discord.ext import commands

class count100(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setupCounter(self, ctx):
        guild = ctx.guild

        await guild.channel("counter 100")

async def setup(bot):
    await bot.add_cog(count100(bot))