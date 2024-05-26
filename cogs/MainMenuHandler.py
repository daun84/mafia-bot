from discord.ext import commands
from loguru import logger


class MainMenuHandler(commands.Cog):
    """
        Description
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """
            Main listener
        """

        # Prevent the bot from replying to itself
        if message.author == self.bot.user:
            return

    @commands.command()
    async def status(self, ctx):
        """
            Returns statistics or something
        """
        await ctx.send(f"{ctx.author.id}")

    @commands.command()
    async def help(self, ctx):
        """
            Returns rules
        """
        await ctx.send("Anarchy")


async def setup(bot):
    await bot.add_cog(MainMenuHandler(bot))
