import discord
from discord.ext import commands
import env
from _datetime import datetime

TOKEN = env.token
testingServers = env.serverList
# bot = discord.Bot

choice1 = ""
choice2 = ""

bingo_position = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5", "D1",
                  "D2", "D3", "D4", "D5", "E1", "E2", "E3", "E4", "E5"]

approved_list = ["A1", "A2", "A3", "A4", "A5", "B1", "B5", "C1", "C5", "D1", "D5", "E1", "E2", "E3", "E4", "E5"]

bingo_dict = {"A1": ["A1", "A5", "E1", "E5"],
              "A2": ["B1", "D5", "E2"],
              "A3": ["C1", "C5", "E3"],
              "A4": ["B5", "D1", "E4"],
              "A5": ["A1", "A5", "E1", "E5"],
              "B1": ["B5", "A2", "E4"],
              "B5": ["A4", "B1", "E2"],
              "C1": ["A3", "C5", "E3"],
              "C5": ["A3", "C1", "E3"],
              "D1": ["A4", "D5", "E2"],
              "D5": ["A2", "D1", "E4"],
              "E1": ["A1", "A5", "E1", "E5"],
              "E2": ["A2", "B5", "D1"],
              "E3": ["A3", "C3", "C5"],
              "E4": ["A4", "B1", "D5"],
              "E5": ["A1", "A5", "E1", "E5"],
              }


class BingoButtonMain(discord.ui.Button):
    def __init__(self, position):
        super().__init__(
            style=discord.ButtonStyle.primary,
            label=position,
            disabled=False
        )

    async def callback(self, interaction: discord.Interaction):
        global choice1
        user = interaction.user
        choice1 = self.label
        new_view = bingo_pairing(self.label, bingo_dict)
        await interaction.response.edit_message(content=f'{user}, your first choice is: {choice1}',
                                                view=new_view)


class BingoButtonFinal(discord.ui.Button):
    def __init__(self, position):
        super().__init__(
            style=discord.ButtonStyle.green,
            label=position,
            disabled=False
        )

    async def callback(self, interaction: discord.Interaction):
        global choice2
        user = interaction.user
        choice2 = self.label
        verify_view = verify_choice("Bingo")
        await interaction.response.edit_message(content=f'{user}, you chose {choice1} as your starting position and '
                                                        f'{choice2} as the ending position. Is this correct?',
                                                view=verify_view)


class BingoButtonDisabled(discord.ui.Button):
    def __init__(self, position):
        super().__init__(
            style=discord.ButtonStyle.gray,
            label=position,
            disabled=True
        )

    async def callback(self, interaction: discord.Interaction):
        return


class VerifyChoicesBingo(discord.ui.Button):
    def __init__(self, label):
        super().__init__(
            style=discord.ButtonStyle.primary,
            label=label,
            disabled=False
        )

    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        channel = interaction.channel
        if self.label == "No":
            await interaction.response.edit_message(content=f'Please try again.',
                                                    view=None)
        else:
            await interaction.response.edit_message(content=f'Your choices were {choice1} to {choice2}. Moving data '
                                                            f'to final position...',
                                                    view=None)
            await channel.send(f'{user}, testing Yes')


class ButtonBingoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=testingServers, description="Display Bingo Board")
    async def bingo(self, ctx: discord.ApplicationContext):
        view = discord.ui.View(timeout=20)

        for location in bingo_position:
            if location in approved_list:
                view.add_item(BingoButtonMain(location))
            else:
                view.add_item(BingoButtonDisabled(location))

        await ctx.respond("Choose your starting point.", view=view)


def bingo_pairing(label: str, data: dict):
    view = discord.ui.View(timeout=20)
    for key, value in data.items():
        if key == label:
            for location in bingo_position:
                if location in value:
                    view.add_item(BingoButtonFinal(location))
                else:
                    view.add_item(BingoButtonDisabled(location))
    return view


def verify_choice(var):
    view = discord.ui.View(timeout=20)
    if var == "Bingo":
        view.add_item(VerifyChoicesBingo("Yes"))
        view.add_item(VerifyChoicesBingo("No"))
        return view
    else:
        print("Error in bingoButtons.verify_choice")
        return


def setup(bot):
    bot.add_cog(ButtonBingoCog(bot))
