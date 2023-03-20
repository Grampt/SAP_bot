import discord
from discord.ext import commands
import env
from _datetime import datetime

TOKEN = env.token
testingServers = env.serverList

choice = ""

weekly_modes = ["Standard", "Hard", "Reverse", "Perfect", "Sloth", "Food", "Level", "Extreme"]


class WeeklyButtonStandardMode(discord.ui.Button):
    def __init__(self, label, row):
        super().__init__(
            style=discord.ButtonStyle.primary,
            label=label,
            row=row,
            disabled=False
        )

    async def callback(self, interaction: discord.Interaction):
        global choice
        user = interaction.user
        choice = self.label
        new_view = verify_choice("Weekly")
        await interaction.response.edit_message(content=f'{user}, you are claiming: {choice}.',
                                                view=new_view)


class WeeklyButtonHardMode(discord.ui.Button):
    def __init__(self, label, row):
        super().__init__(
            style=discord.ButtonStyle.green,
            label=label,
            row=row,
            disabled=False
        )

    async def callback(self, interaction: discord.Interaction):
        global choice
        user = interaction.user
        choice = self.label
        new_view = verify_choice("Weekly")
        await interaction.response.edit_message(content=f'{user}, you are claiming: {choice}.',
                                                view=new_view)


class VerifyChoicesWeekly(discord.ui.Button):
    def __init__(self, label, style):
        super().__init__(
            style=style,
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
            await interaction.response.edit_message(content=f'You completed the {choice} challenge. Moving data '
                                                            f'to final position...',
                                                    view=None)
            await channel.send(f'{user}, testing Yes')


class ButtonWeeklyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=testingServers, description="Display Weekly Options")
    async def weekly(self, ctx: discord.ApplicationContext):
        view = discord.ui.View(timeout=20)
        row = 0
        but_count = 0
        for mode_standard in weekly_modes:
            view.add_item(WeeklyButtonStandardMode(mode_standard, row))
            but_count += 1
            if but_count == 4:
                row += 1
                but_count = 0
        for mode in weekly_modes:
            mode_hard = mode + ":Hard"
            view.add_item(WeeklyButtonHardMode(mode_hard, row))
            but_count += 1
            if but_count == 4:
                row += 1
                but_count = 0

        await ctx.respond("Which challenge are you claiming?", view=view)


def verify_choice(var):
    view = discord.ui.View(timeout=20)
    if var == "Weekly":
        view.add_item(VerifyChoicesWeekly("Yes", discord.ButtonStyle.green))
        view.add_item(VerifyChoicesWeekly("No", discord.ButtonStyle.red))
        return view
    else:
        print("Error in bingoButtons.verify_choice")
        return


def setup(bot):
    bot.add_cog(ButtonWeeklyCog(bot))
