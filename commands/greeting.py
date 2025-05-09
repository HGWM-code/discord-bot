from discord.ext import commands
from discord import app_commands

class Greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hello", description="say hello!")
    async def hello(self, interaction):
        await interaction.response.send_message("hello")

async def setup(bot):
    await bot.add_cog(Greeting(bot))
