import asyncio

import discord
import env
from _datetime import datetime

TOKEN = env.token
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

class WeeklyButton(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=10)
        self.ctx = ctx

    @discord.ui.button(label="Standard", style=discord.ButtonStyle.primary, row=0)
    async def button_callback(self, button, interaction):
        author, author_id, guild, guild_id = get_user_id(interaction)
        for child in self.children:  # loop through all the children of the view
            child.disabled = True  # set the button to disabled
        await interaction.response.edit_message(view=None, content="You clicked the Standard button!")
        print(author, author_id, guild, guild_id)

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


@bot.slash_command(guild_ids=testingServers, name="weekly", description="Claim the accomplishment")
async def button(ctx):
    await ctx.respond("Which did you complete?", view=WeeklyButton(ctx))


def get_user_id(ctx):
    author_name = ctx.user
    author_id = ctx.id
    guild = ctx.guild
    guild_id = ctx.guild.id
    return author_name, author_id, guild, guild_id


bot.run(TOKEN)
