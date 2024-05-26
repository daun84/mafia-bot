from discord.ext import commands
from models.GameContext import GameContext


class GameLoopHandler(commands.Cog):
    """
        Description
    """
    def __init__(self, bot):
        self.bot = bot
        self.game_context: GameContext = None

    @commands.command()
    async def action(self, ctx):
        """
            Description
        """
        pass

    @commands.command()
    async def create_game(self, ctx):
        """
            creates game lol
        """
        pass

    @commands.command()
    async def join_game(self, ctx):
        """
            asdads
        """
        pass



async def setup(bot):
    await bot.add_cog(GameLoopHandler(bot))
