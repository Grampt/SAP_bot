import asyncio

import discord
import env
from _datetime import datetime

# TOKEN = env.token
testingServers = env.serverList
bot = discord.Bot()

buttons_selected = 0
button_one = ""
button_two = ""
button_week = ""

currentTime = datetime.now()


async def verify_bingo(interaction):
    await interaction.response.send_message(view=VerifyBingo,
                                            content=f'Your choices were {button_one} and {button_two}. Are you sure '
                                                    f'these choices are what you want?')
    return


async def verify_weekly(interaction):
    await interaction.response.send_message(view=VerifyWeekly,
                                            content=f'Your choice was {button_week}. Are you sure this choice is '
                                                    f'what you want?')
    return


async def choice_one(label: str, interaction, new_view):
    if buttons_selected > 0:
        print("Choice 1: Choice already selected.")
    global button_one
    button_one = label
    author = interaction.user
    increase_button_selected()
    await interaction.response.edit_message(view=new_view(interaction),
                                            content=f'{author}, your first choice was {label}! Please select '
                                                    f'another option')


async def choice_two(label: str, interaction):
    if buttons_selected < 1:
        print("Choice 2: No choices selected.")
        return
    global button_two
    button_two = label
    author = interaction.user
    reset_button_selected()
    await interaction.response.edit_message(view=VerifyBingo(interaction),
                                            content=f'{author}, your choices were {button_one} and {button_two}. '
                                                    f'Are you sure these choices are that you want?')


def increase_button_selected():
    global buttons_selected
    buttons_selected = 1
    return buttons_selected


def reset_button_selected():
    global buttons_selected
    buttons_selected = 0
    return buttons_selected


# class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
#     @discord.ui.button(label="Standard", style=discord.ButtonStyle.primary, row=0) # Create a button with the label
#     "😎 Click me!" with color Blurple
#     async def button_callback(self, button, interaction):
#         await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked
#
#     @discord.ui.button(label="Food", style=discord.ButtonStyle.primary, row=1)
#     async def button_callback(self, button, interaction):
#         await interaction.response.send_message("You clicked the button!")


class WeeklyButtons(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=10)
        self.ctx = ctx

    @discord.ui.button(label="Standard", style=discord.ButtonStyle.primary, row=0)
    async def button_callback(self, button, interaction):
        author, author_id, guild, guild_id, channel = get_user_id(interaction)
        for child in self.children:  # loop through all the children of the view
            child.disabled = True  # set the button to disabled
        await interaction.response.edit_message(view=None, content="You clicked the Standard button!")
        await channel.send('hello')
        print(author, author_id, guild, guild_id, channel)

    @discord.ui.button(label="Hard", style=discord.ButtonStyle.primary, row=0)
    async def second_button_callback(self, button, interaction):
        get_user_id(interaction.user)
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=None, content="You clicked the Hard button!")

    @discord.ui.button(label="Reverse", style=discord.ButtonStyle.primary, row=0)
    async def third_button_callback(self, button, interaction):
        get_user_id(interaction.user)
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=None, content="You clicked the Reverse button!")

    @discord.ui.button(label="Perfect", style=discord.ButtonStyle.primary, row=0)
    async def fourth_button_callback(self, button, interaction):
        get_user_id(interaction.user)
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=None, content="You clicked the Perfect button!")

    @discord.ui.button(label="Sloth", style=discord.ButtonStyle.primary, row=1)
    async def fifth_button_callback(self, button, interaction):
        get_user_id(interaction.user)
        for child in self.children:  # loop through all the children of the view
            child.disabled = True  # set the button to disabled
        await interaction.response.edit_message(view=None, content="You clicked the Sloth button!")

    @discord.ui.button(label="Food", style=discord.ButtonStyle.primary, row=1)
    async def sixth_button_callback(self, button, interaction):
        get_user_id(interaction.user)
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=None, content="You clicked the Food button!")

    @discord.ui.button(label="Level", style=discord.ButtonStyle.primary, row=1)
    async def seventh_button_callback(self, button, interaction):
        get_user_id(interaction.user)
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=None, content="You clicked the Level button!")

    @discord.ui.button(label="Extreme", style=discord.ButtonStyle.primary, row=1)
    async def eighth_button_callback(self, button, interaction):
        get_user_id(interaction.user)
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=None, content="You clicked the Extreme button!")

    async def on_timeout(self):
        await self.ctx.send("Timed Out")

    async def interaction_check(self, interaction) -> bool:
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("Hey, stop that", ephemeral=True)
            return False
        else:
            return True

    async def on_error(self, error, item, interaction):
        await interaction.response.send_message(str(error))


class NewWeekButtons(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=10)
        self.ctx = ctx

    @discord.ui.button(label="Weekly", style=discord.ButtonStyle.primary, row=0)
    async def button_callback(self, button, interaction):
        author, author_id, guild, guild_id, channel = get_user_id(interaction)
        for child in self.children:  # loop through all the children of the view
            child.disabled = True  # setter the button to disabled
        await interaction.response.edit_message(view=None, content="You clicked the Weekly button!")
        await channel.send('hello')
        print(author, author_id, guild, guild_id, channel)

    @discord.ui.button(label="Bingo", style=discord.ButtonStyle.primary, row=0)
    async def second_button_callback(self, button, interaction):
        get_user_id(interaction.user)
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=None, content="You clicked the Bingo button!")

    @discord.ui.button(label="Full Reset", style=discord.ButtonStyle.primary, row=0)
    async def third_button_callback(self, button, interaction):
        get_user_id(interaction.user)
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=None, content="You clicked the Full Reset button!")

    async def on_timeout(self):
        await self.ctx.send("Timed Out")

    async def interaction_check(self, interaction) -> bool:
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("Hey, stop that", ephemeral=True)
            return False
        else:
            return True

    # async def on_error(self, error, item, interaction):
    #     await interaction.response.send_message(str(error))


class BingoButtonsMain(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=10)
        self.ctx = ctx

    @discord.ui.button(label="A1", style=discord.ButtonStyle.primary, row=0)
    async def button1_callback(self, button, interaction):
        await choice_one("A1", interaction, BingoCorners)
        return

    @discord.ui.button(label="A2", style=discord.ButtonStyle.primary, row=0)
    async def button2_callback(self, button, interaction):
        await choice_one("A2", interaction, BingoCorners)
        return

    @discord.ui.button(label="A3", style=discord.ButtonStyle.primary, row=0)
    async def button3_callback(self, button, interaction):
        await choice_one("A3", interaction, BingoCorners)
        return

    @discord.ui.button(label="A4", style=discord.ButtonStyle.primary, row=0)
    async def button4_callback(self, button, interaction):
        await choice_one("A4", interaction, BingoCorners)
        return

    @discord.ui.button(label="A5", style=discord.ButtonStyle.primary, row=0)
    async def button5_callback(self, button, interaction):
        await choice_one("A5", interaction, BingoCorners)
        return

    @discord.ui.button(label="B1", style=discord.ButtonStyle.primary, row=1)
    async def button6_callback(self, button, interaction):
        await choice_one("B1", interaction, BingoCorners)
        return

    @discord.ui.button(label="B2", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def button7_callback(self, button, interaction):
        return

    @discord.ui.button(label="B3", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def button8_callback(self, button, interaction):
        return

    @discord.ui.button(label="B4", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def button9_callback(self, button, interaction):
        return

    @discord.ui.button(label="B5", style=discord.ButtonStyle.primary, row=1)
    async def button10_callback(self, button, interaction):
        await choice_one("B5", interaction, BingoCorners)
        return

    @discord.ui.button(label="C1", style=discord.ButtonStyle.primary, row=2)
    async def button11_callback(self, button, interaction):
        await choice_one("C1", interaction, BingoCorners)
        return

    @discord.ui.button(label="C2", style=discord.ButtonStyle.primary, row=2, disabled=True)
    async def button12_callback(self, button, interaction):
        return

    @discord.ui.button(label="C3", style=discord.ButtonStyle.primary, row=2, disabled=True)
    async def button13_callback(self, button, interaction):
        return

    @discord.ui.button(label="C4", style=discord.ButtonStyle.primary, row=2, disabled=True)
    async def button14_callback(self, button, interaction):
        return

    @discord.ui.button(label="C5", style=discord.ButtonStyle.primary, row=2)
    async def button15_callback(self, button, interaction):
        await choice_one("C5", interaction, BingoCorners)
        return

    @discord.ui.button(label="D1", style=discord.ButtonStyle.primary, row=3)
    async def button16_callback(self, button, interaction):
        await choice_one("D1", interaction, BingoCorners)
        return

    @discord.ui.button(label="D2", style=discord.ButtonStyle.primary, row=3, disabled=True)
    async def button17_callback(self, button, interaction):
        return

    @discord.ui.button(label="D3", style=discord.ButtonStyle.primary, row=3, disabled=True)
    async def button18_callback(self, button, interaction):
        return

    @discord.ui.button(label="D4", style=discord.ButtonStyle.primary, row=3, disabled=True)
    async def button19_callback(self, button, interaction):
        return

    @discord.ui.button(label="D5", style=discord.ButtonStyle.primary, row=3)
    async def button20_callback(self, button, interaction):
        await choice_one("D5", interaction, BingoCorners)
        return

    @discord.ui.button(label="E1", style=discord.ButtonStyle.primary, row=4)
    async def button21_callback(self, button, interaction):
        await choice_one("E1", interaction, BingoCorners)
        return

    @discord.ui.button(label="E2", style=discord.ButtonStyle.primary, row=4)
    async def button22_callback(self, button, interaction):
        await choice_one("E2", interaction, BingoCorners)
        return

    @discord.ui.button(label="E3", style=discord.ButtonStyle.primary, row=4)
    async def button23_callback(self, button, interaction):
        await choice_one("E3", interaction, BingoCorners)
        return

    @discord.ui.button(label="E4", style=discord.ButtonStyle.primary, row=4)
    async def button24_callback(self, button, interaction):
        await choice_one("E4", interaction, BingoCorners)
        return

    @discord.ui.button(label="E5", style=discord.ButtonStyle.primary, row=4)
    async def button25_callback(self, button, interaction):
        await choice_one("E5", interaction, BingoCorners)
        return

    # async def on_timeout(self):
    #     await self.ctx.message_send("Timeout")

    async def interaction_check(self, interaction) -> bool:
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("Hey, stop that", ephemeral=True)
            return False
        else:
            return True

    # async def on_error(self, error, item, interaction):
    #     await interaction.response.send_message(str(error))

    @staticmethod
    async def disable_buttons(var):
        global buttons_selected
        global setter

        if buttons_selected < 1:
            setter = [[False, False, False, False, False],
                      [False, True, True, True, False],
                      [False, True, True, True, False],
                      [False, True, True, True, False],
                      [False, False, False, False, False]]
            return setter
        else:
            match var:
                case "A2":
                    setter = [[True, True, True, True, True],
                              [False, True, True, True, True],
                              [True, True, True, True, True],
                              [True, True, True, True, False],
                              [True, False, True, True, True]]
                    return setter
                case "A3":
                    setter = [[True, True, True, True, True],
                              [True, True, True, True, True],
                              [False, True, True, True, False],
                              [True, True, True, True, True],
                              [True, True, False, True, True]]
                    return setter
                case "A4":
                    setter = [[True, True, True, True, True],
                              [True, True, True, True, False],
                              [True, True, True, True, True],
                              [False, True, True, True, True],
                              [True, True, True, False, True]]
                    return setter
                case "B1":
                    setter = [[True, False, True, True, True],
                              [True, True, True, True, False],
                              [True, True, True, True, True],
                              [True, True, True, True, True],
                              [True, True, True, False, True]]
                    return setter
                case "B5":
                    setter = [[True, True, True, False, True],
                              [False, True, True, True, True],
                              [True, True, True, True, True],
                              [True, True, True, True, True],
                              [True, False, True, True, True]]
                    return setter
                case "C1":
                    setter = [[True, True, False, True, True],
                              [True, True, True, True, True],
                              [True, True, True, True, False],
                              [True, True, True, True, True],
                              [True, True, False, True, True]]
                    return setter
                case "C5":
                    setter = [[True, True, False, True, True],
                              [True, True, True, True, True],
                              [False, True, True, True, True],
                              [True, True, True, True, True],
                              [True, True, False, True, True]]
                    return setter
                case "D1":
                    setter = [[True, True, True, False, True],
                              [True, True, True, True, True],
                              [True, True, True, True, True],
                              [True, True, True, True, False],
                              [True, False, True, True, True]]
                    return setter
                case "E2":
                    setter = [[True, False, True, True, True],
                              [True, True, True, True, False],
                              [True, True, True, True, True],
                              [False, True, True, True, True],
                              [True, True, True, True, True]]
                    return setter
                case "E3":
                    setter = [[True, True, False, True, True],
                              [True, True, True, True, True],
                              [False, True, True, True, False],
                              [True, True, True, True, True],
                              [True, True, True, True, True]]
                    return setter
                case "E4":
                    setter = [[True, True, True, False, True],
                              [False, True, True, True, True],
                              [True, True, True, True, True],
                              [True, True, True, True, False],
                              [True, True, True, True, True]]
                    return setter
                case _:
                    setter = [[False, True, True, True, False],
                              [True, True, True, True, True],
                              [True, True, True, True, True],
                              [True, True, True, True, True],
                              [False, True, True, True, False]]
                    return setter


class BingoCorners(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=10)
        self.ctx = ctx

    @discord.ui.button(label="A1", style=discord.ButtonStyle.primary, row=0, disabled=False)
    async def button1_callback(self, button, interaction):
        await choice_two("A1", interaction)
        return

    @discord.ui.button(label="A2", style=discord.ButtonStyle.primary, row=0, disabled=True)
    async def button2_callback(self, button, interaction):
        return

    @discord.ui.button(label="A3", style=discord.ButtonStyle.primary, row=0, disabled=True)
    async def button3_callback(self, button, interaction):
        return

    @discord.ui.button(label="A4", style=discord.ButtonStyle.primary, row=0, disabled=True)
    async def button4_callback(self, button, interaction):
        return

    @discord.ui.button(label="A5", style=discord.ButtonStyle.primary, row=0, disabled=False)
    async def button5_callback(self, button, interaction):
        await choice_two("A5", interaction)
        return

    @discord.ui.button(label="B1", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def button6_callback(self, button, interaction):
        return

    @discord.ui.button(label="B2", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def button7_callback(self, button, interaction):
        return

    @discord.ui.button(label="B3", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def button8_callback(self, button, interaction):
        return

    @discord.ui.button(label="B4", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def button9_callback(self, button, interaction):
        return

    @discord.ui.button(label="B5", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def button10_callback(self, button, interaction):
        return

    @discord.ui.button(label="C1", style=discord.ButtonStyle.primary, row=2, disabled=True)
    async def button11_callback(self, button, interaction):
        return

    @discord.ui.button(label="C2", style=discord.ButtonStyle.primary, row=2, disabled=True)
    async def button12_callback(self, button, interaction):
        return

    @discord.ui.button(label="C3", style=discord.ButtonStyle.primary, row=2, disabled=True)
    async def button13_callback(self, button, interaction):
        return

    @discord.ui.button(label="C4", style=discord.ButtonStyle.primary, row=2, disabled=True)
    async def button14_callback(self, button, interaction):
        return

    @discord.ui.button(label="C5", style=discord.ButtonStyle.primary, row=2, disabled=True)
    async def button15_callback(self, button, interaction):
        return

    @discord.ui.button(label="D1", style=discord.ButtonStyle.primary, row=3, disabled=True)
    async def button16_callback(self, button, interaction):
        return

    @discord.ui.button(label="D2", style=discord.ButtonStyle.primary, row=3, disabled=True)
    async def button17_callback(self, button, interaction):
        return

    @discord.ui.button(label="D3", style=discord.ButtonStyle.primary, row=3, disabled=True)
    async def button18_callback(self, button, interaction):
        return

    @discord.ui.button(label="D4", style=discord.ButtonStyle.primary, row=3, disabled=True)
    async def button19_callback(self, button, interaction):
        return

    @discord.ui.button(label="D5", style=discord.ButtonStyle.primary, row=3, disabled=True)
    async def button20_callback(self, button, interaction):
        return

    @discord.ui.button(label="E1", style=discord.ButtonStyle.primary, row=4, disabled=False)
    async def button21_callback(self, button, interaction):
        await choice_two("E1", interaction)
        return

    @discord.ui.button(label="E2", style=discord.ButtonStyle.primary, row=4, disabled=True)
    async def button22_callback(self, button, interaction):
        return

    @discord.ui.button(label="E3", style=discord.ButtonStyle.primary, row=4, disabled=True)
    async def button23_callback(self, button, interaction):
        return

    @discord.ui.button(label="E4", style=discord.ButtonStyle.primary, row=4, disabled=True)
    async def button24_callback(self, button, interaction):
        return

    @discord.ui.button(label="E5", style=discord.ButtonStyle.primary, row=4, disabled=False)
    async def button25_callback(self, button, interaction):
        await choice_two("E5", interaction)
        return


class BingoDisabled(discord.ui.View):
    global button_one
    global button_two
    global buttons_selected

    def __init__(self, ctx):
        super().__init__(timeout=10)
        self.ctx = ctx

    @discord.ui.button(label="A1", style=discord.ButtonStyle.primary, row=0, disabled=True)
    async def button1_callback(self, button, interaction):
        return

    @discord.ui.button(label="A2", style=discord.ButtonStyle.primary, row=0, disabled=True)
    async def button2_callback(self, button, interaction):
        return

    @discord.ui.button(label="A3", style=discord.ButtonStyle.primary, row=0, disabled=True)
    async def button3_callback(self, button, interaction):
        return

    @discord.ui.button(label="A4", style=discord.ButtonStyle.primary, row=0, disabled=True)
    async def button4_callback(self, button, interaction):
        return

    @discord.ui.button(label="A5", style=discord.ButtonStyle.primary, row=0, disabled=True)
    async def button5_callback(self, button, interaction):
        return

    @discord.ui.button(label="B1", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def button6_callback(self, button, interaction):
        return

    @discord.ui.button(label="B2", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def button7_callback(self, button, interaction):
        return

    @discord.ui.button(label="B3", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def button8_callback(self, button, interaction):
        return

    @discord.ui.button(label="B4", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def button9_callback(self, button, interaction):
        return

    @discord.ui.button(label="B5", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def button10_callback(self, button, interaction):
        return

    @discord.ui.button(label="C1", style=discord.ButtonStyle.primary, row=2, disabled=True)
    async def button11_callback(self, button, interaction):
        return

    @discord.ui.button(label="C2", style=discord.ButtonStyle.primary, row=2, disabled=True)
    async def button12_callback(self, button, interaction):
        return

    @discord.ui.button(label="C3", style=discord.ButtonStyle.primary, row=2, disabled=True)
    async def button13_callback(self, button, interaction):
        return

    @discord.ui.button(label="C4", style=discord.ButtonStyle.primary, row=2, disabled=True)
    async def button14_callback(self, button, interaction):
        return

    @discord.ui.button(label="C5", style=discord.ButtonStyle.primary, row=2, disabled=True)
    async def button15_callback(self, button, interaction):
        return

    @discord.ui.button(label="D1", style=discord.ButtonStyle.primary, row=3, disabled=True)
    async def button16_callback(self, button, interaction):
        return

    @discord.ui.button(label="D2", style=discord.ButtonStyle.primary, row=3, disabled=True)
    async def button17_callback(self, button, interaction):
        return

    @discord.ui.button(label="D3", style=discord.ButtonStyle.primary, row=3, disabled=True)
    async def button18_callback(self, button, interaction):
        return

    @discord.ui.button(label="D4", style=discord.ButtonStyle.primary, row=3, disabled=True)
    async def button19_callback(self, button, interaction):
        return

    @discord.ui.button(label="D5", style=discord.ButtonStyle.primary, row=3, disabled=True)
    async def button20_callback(self, button, interaction):
        return

    @discord.ui.button(label="E1", style=discord.ButtonStyle.primary, row=4, disabled=True)
    async def button21_callback(self, button, interaction):
        return

    @discord.ui.button(label="E2", style=discord.ButtonStyle.primary, row=4, disabled=True)
    async def button22_callback(self, button, interaction):
        return

    @discord.ui.button(label="E3", style=discord.ButtonStyle.primary, row=4, disabled=True)
    async def button23_callback(self, button, interaction):
        return

    @discord.ui.button(label="E4", style=discord.ButtonStyle.primary, row=4, disabled=True)
    async def button24_callback(self, button, interaction):
        return

    @discord.ui.button(label="E5", style=discord.ButtonStyle.primary, row=4, disabled=True)
    async def button25_callback(self, button, interaction):
        return


class VerifyBingo(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=10)
        self.ctx = ctx

    @discord.ui.button(label="Yes", style=discord.ButtonStyle.primary, row=0, disabled=False)
    async def button1_callback(self, button, interaction):
        author = interaction.user
        channel = interaction.channel
        await interaction.response.edit_message(view=None, content="Processing...")
        await channel.send(f'{author}, Testing Yes')
        return

    @discord.ui.button(label="No", style=discord.ButtonStyle.primary, row=0, disabled=False)
    async def button2_callback(self, button, interaction):
        author = interaction.user
        channel = interaction.channel
        await interaction.response.edit_message(view=None, content="Processing...")
        await channel.send(f'{author}, Testing No')
        return


class VerifyWeekly(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=10)
        self.ctx = ctx

    @discord.ui.button(label="Yes", style=discord.ButtonStyle.primary, row=0, disabled=False)
    async def button1_callback(self, button, interaction):
        return

    @discord.ui.button(label="No", style=discord.ButtonStyle.primary, row=0, disabled=False)
    async def button2_callback(self, button, interaction):
        return


def get_user_id(ctx):
    author_name = ctx.user
    author_id = ctx.id
    guild = ctx.guild
    guild_id = ctx.guild.id
    channel = ctx.channel
    return author_name, author_id, guild, guild_id, channel
