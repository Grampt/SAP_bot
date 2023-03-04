import asyncio

import discord
import env
from _datetime import datetime

# TOKEN = env.token
testingServers = env.serverList
bot = discord.Bot()


currentTime = datetime.now()


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


class BingoButtons(discord.ui.View):
    buttons_selected = 0
    button_one = "this"
    button_two = "this"

    #    label_list = ["A1", "A2", "A3", "A4", "A5", "B1", "B5", "C1", "C5", "D1", "D5", "E1", "E2", "E3", "E4", "E5"]

    def __init__(self, ctx, buttons_selected, button_one, button_two):
        super().__init__(timeout=10)
        self.ctx = ctx
        self.buttons_selected = buttons_selected
        self.button_one = button_one
        self.button_two = button_two

    def increase_button_selected(self):
        self.buttons_selected += 1

    def reset_button_selected(self):
        self.buttons_selected = 0

    def set_button_one(self, var):
        self.button_one = var

    def set_button_two(self, var):
        self.button_two = var

    @discord.ui.button(label="A1", style=discord.ButtonStyle.primary, row=0)
    async def button_callback(self, button, interaction):
        label: str = "A1"
        author = interaction.user
        for child in self.children:
            if child.label != {"A1", "A5", "E1", "E5"}:
                child.disabled = True
        if self.buttons_selected < 1:
            await interaction.response.edit_message(content=f'{author}, your first choice was {label}! Please select '
                                                            f'another option')
            self.set_button_one(label)
            self.increase_button_selected()
        else:
            self.set_button_two(label)
            self.reset_button_selected()
            await interaction.response.edit_message(view=None, content=f'{author}, your first choice was '
                                                                       f'{self.button_one} and '
                                                                       f'your second choice was {self.button_two}!')

    @discord.ui.button(label="A2", style=discord.ButtonStyle.primary, row=0)
    async def second_button_callback(self, button, interaction):
        get_user_id(interaction.user)
        for child in self.children:
            if child.label != {"B1", "D5", "E2"}:
                child.disabled = True
        if self.buttons_selected < 1:
            await interaction.response.edit_message(content="Your first choice was A2! Please select another option")
            self.set_button_one("A2")
            self.increase_button_selected()
        else:
            await interaction.response.edit_message(view=None, content="Your first choice was A2! Please select "
                                                                       "another option")
            self.set_button_two("A2")
            self.increase_button_selected()

    @discord.ui.button(label="A3", style=discord.ButtonStyle.primary, row=0)
    async def third_button_callback(self, button, interaction):
        get_user_id(interaction.user)
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=None, content="You clicked the Reverse button!")

    @discord.ui.button(label="A4", style=discord.ButtonStyle.primary, row=0)
    async def fourth_button_callback(self, button, interaction):
        get_user_id(interaction.user)
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=None, content="You clicked the Perfect button!")

    @discord.ui.button(label="A5", style=discord.ButtonStyle.primary, row=0)
    async def fifth_button_callback(self, button, interaction):
        get_user_id(interaction.user)
        for child in self.children:  # loop through all the children of the view
            child.disabled = True  # set the button to disabled
        await interaction.response.edit_message(view=None, content="You clicked the Sloth button!")

    @discord.ui.button(label="B1", style=discord.ButtonStyle.primary, row=1)
    async def sixth_button_callback(self, button, interaction):
        get_user_id(interaction.user)
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=None, content="You clicked the Food button!")

    @discord.ui.button(label="B2", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def seventh_button_callback(self, button, interaction):
        return

    @discord.ui.button(label="B3", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def eighth_button_callback(self, button, interaction):
        return

    @discord.ui.button(label="B4", style=discord.ButtonStyle.primary, row=1, disabled=True)
    async def ninth_button_callback(self, button, interaction):
        return

    @discord.ui.button(label="B5", style=discord.ButtonStyle.primary, row=1)
    async def tenth_button_callback(self, button, interaction):
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
            child.disabled = True  # set the button to disabled
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

    async def on_error(self, error, item, interaction):
        await interaction.response.send_message(str(error))


# @bot.slash_command(guild_ids=testingServers, name="weekly", description="Claim the accomplishment")
# async def button(ctx):
#     await ctx.respond("Which did you complete?", view=WeeklyButton(ctx))


def get_user_id(ctx):
    author_name = ctx.user
    author_id = ctx.id
    guild = ctx.guild
    guild_id = ctx.guild.id
    channel = ctx.channel
    return author_name, author_id, guild, guild_id, channel

# bot.run(TOKEN)
