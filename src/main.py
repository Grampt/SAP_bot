import discord
import sqlite3
import time
import numpy as np
from discord import option
from discord import commands
from discord import default_permissions
import env
import datetime
import turtle
from weeklySQL import WeeklyInput
import buttonLayouts


TOKEN = env.token
testingServers = env.serverList
bot = discord.Bot()

database = ':memory:'
# con = sqlite3.connect("SAP_Challenge.db")
# c = con.cursor()

weekly_id_current = 0
challenge_type = "weekly"
current_weekly_date = '2023-04-28 09:55:20.156'

tables = ['temp_weekly', 'weekly', 'bingo', 'temp_bingo', 'score', 'mode_dim', 'week_dim', 'achievement_dim']


#   Notes on Table/Column/Row interactions, Foreign Keys
#   Weekly: compound_id is a concatenation of the
#
#   week_dim: make the table, query compound key of most recent weekly_id per game_mode per server_id, write to table
#
#
#
#
# fall


def create_connection(db_file):
    connect = None
    try:
        connect = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return connect


def pause(a: int):
    if a > 5:
        a == 5
    time.sleep(a)
    return


def check_table_exists(dbcon, table_name):
    """Checks to see if the database already exists"""
    dbcurs = dbcon.cursor()
    table = dbcurs.execute("""SELECT name FROM sqlite_schema WHERE type ='table' AND name = (?)""",
                           (table_name,)).fetchall()
    print(dbcurs.fetchall())
    if table == []:
        print(str(table_name) + " doesn't exist.")
        dbcurs.close()
        return False
    else:
        print(str(table_name) + " exists.")
        dbcurs.close()
        return True

#   Notes on Table/Column/Row interactions, Foreign Keys
#   Weekly: compound_id is a concatenation of the
#
#   week_dim: make the table, query compound key of most recent weekly_id per game_mode per server_id, write to table
#
#
#
#
# fall


def close_conn(connection_link):
    cur = connection_link.cursor()
    cur.close()
    return


def make_db():
    # "Make the weekly tables"
    connect = create_connection(database)
    curs = connect.cursor()
    if check_table_exists(connect, "weekly"):
        print("weekly exists")
    else:
        curs.execute("""CREATE TABLE weekly (
                        compound_id text,
                        user_id integer,
                        weekly_id integer,
                        mode integer,
                        score integer,
                        server_id integer,
                        entry_date text,
                        game_mode text,
                        PRIMARY KEY(user_id, weekly_id, mode, server_id, game_mode)
                        )""")
        print("weekly created")

    if check_table_exists(connect, "temp_weekly"):
        print("temp_weekly exists")
    else:
        curs.execute("""CREATE TABLE temp_weekly (
                        compound_id text,
                        user_id integer,
                        weekly_id integer,
                        mode integer,
                        score integer,
                        server_id integer,
                        entry_date text,
                        game_mode text,
                        PRIMARY KEY(user_id, weekly_id, mode, server_id, game_mode)
                        )""")
        print("temp_weekly created")
    # "Make the bingo tables"
    if check_table_exists(connect, "bingo"):
        print("bingo exists")
    else:
        curs.execute("""CREATE TABLE bingo (
                        compound_id text,
                        user_id integer,
                        weekly_id integer,
                        achievement integer,
                        ranking integer,
                        score integer,
                        server_id integer,
                        entry_date text,
                        game_mode text,
                        PRIMARY KEY(weekly_id, achievement, ranking, server_id, game_mode)
                        )""")
        print("bingo created")
    if check_table_exists(connect, "temp_bingo"):
        print("temp_bingo exists")
    else:
        curs.execute("""CREATE TABLE temp_bingo (
                        compound_id text,
                        user_id integer,
                        weekly_id integer,
                        achievement integer,
                        ranking integer,
                        score integer,
                        server_id integer,
                        entry_date text,
                        game_mode text,
                        PRIMARY KEY(weekly_id, achievement, ranking, server_id, game_mode)
                        )""")
        print("temp_bingo created")
    # "Make the auxiliary tables"
    if check_table_exists(connect, "score"):
        print("score exists")
    else:
        curs.execute("""CREATE TABLE score (
                        user_id integer,
                        server_id integer,
                        entry_date text,
                        points integer,
                        weekly_id integer,
                        PRIMARY KEY(user_id, server_id)
                        )""")
        print("score created")
    if check_table_exists(connect, "mode_dim"):
        print("mode_dim exists")
    else:
        curs.execute("""CREATE TABLE mode_dim (
                        mode integer,
                        description text,
                        points integer,
                        PRIMARY KEY(mode)
                        )""")
        print("mode_dim created")
    if check_table_exists(connect, "week_dim"):
        print("week_dim exists")
    else:
        curs.execute("""CREATE TABLE week_dim (
                        weekly_id integer,
                        server_id integer,
                        game_mode text,
                        start_date text,
                        PRIMARY KEY(weekly_id, server_id, game_mode)
                        )""")
        print("week_dim created")
    if check_table_exists(connect, "achievement_dim"):
        print("achievement_dim exists")
    else:
        curs.execute("""CREATE TABLE achievement_dim (
                        achievement integer,
                        server_id integer,
                        points integer,
                        rank integer,
                        start_coord text,
                        end_coord text,
                        description text,
                        PRIMARY KEY(achievement, server_id)
                        )""")
        print("achievement_dim created")
    if check_table_exists(connect, "img_dim"):
        print("img_dim exists")
    else:
        curs.execute("""CREATE TABLE img_dim (
                        server_id integer,
                        weekly_id integer,
                        img blob,
                        PRIMARY KEY(server_id, weekly_id)
                        )""")
        print("img_dim created")
    if check_table_exists(connect, "team_achieve_dim"):
        print("team_achieve dim exists")
    else:
        curs.execute("""CREATE TABLE team_achieve_dim (
                        achieve_num integer,
                        point_value int,
                        PRIMARY KEY(achieve_num)
                        )""")
        print("team_achieve_dim created")
    print("\nDatabase is made!")
    close_conn(connect)
    return


def check_for_copy():
    return


def get_game_attr(ctx, week_id, mode_num):
    author_name = ctx.user  # 0
    author_id = ctx.user.id  # 1
    guild = ctx.guild  # 2
    guild_id = ctx.guild.id  # 3
    weekly_id = week_id  # 4
    entry_date = datetime.datetime.now()  # 5
    mode = mode_num  # 6
    # print(author_name, author_id, guild, guild_id, weekly_id, entry_date, mode)
    return [author_name, author_id, guild, guild_id, weekly_id, entry_date, mode]


def get_table_data(dbcon, challenge_name, user_data):
    dbcurs = dbcon.cursor()
    author_id = user_data.user.id
    if challenge_name == "weekly":
        dbcurs.execute("SELECT * FROM temp_weekly WHERE user_id=:user_id", {'user_id': author_id})
        return dbcurs.fetchall()
    else:
        dbcurs.execute("SELECT * FROM temp_bingo WHERE user_id=:user_id", {'user_id': author_id})
        return dbcurs.fetchall()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}.")


# General User Commands
@bot.slash_command(guild_ids=testingServers, name="work", description="Checks to see if I am online")
async def work(ctx):
    await ctx.respond(f"I am working! \n\nLatency: {bot.latency * 1000} ms.")


@bot.slash_command(name="greet", description='Greet Someone!')
@option("name",
        description="Enter your friend's name",
        required=False,
        default='')
async def greet(ctx):
    author_name = str(ctx.author)
    name = author_name[:-5]
    await ctx.respond(f"Hello {name}!")


@bot.slash_command(guild_ids=testingServers, name="score", description="Get my score")
async def work(ctx):
    await ctx.respond(f"Here is your data:")
    con = create_connection(database)
    print(get_table_data(con, challenge_type, ctx))
    close_conn(con)


# @bot.slash_command(guild_ids=testingServers, name="weekly", description="Claim a weekly win")
# async def work(ctx, mode):
#     mod_str = "You claimed the " + str(mode) + " mode!"
#     try:
#         WeeklyInput.input_temp_weekly(get_game_attr(ctx, weekly_id_current, mode), con, weekly_id_current)
#         await ctx.respond(f'{mod_str}')
#     except sqlite3.IntegrityError as e:
#         await ctx.respond(f'You have completed this challenge already this week.')


@bot.slash_command(guild_ids=testingServers, name="weekly", description="Claim the accomplishment")
async def button(ctx):
    await ctx.respond("Which did you complete?", view=buttonLayouts.WeeklyButtons(ctx))


@bot.slash_command(guild_ids=testingServers, name="bingo", description="Claim the accomplishment")
async def button(ctx):
    await ctx.respond("Which did you complete?", view=buttonLayouts.BingoButtonsMain(ctx))


# Admin Commands
@bot.slash_command(guild_ids=testingServers, name="new_week",
                   description="Start a new challenge event! Weekly or Bingo")
@default_permissions(administrator=True)
async def button(ctx):
    await ctx.respond("What challenge do we want this week?", view=buttonLayouts.NewWeekButtons(ctx))


@bot.slash_command(guild_ids=testingServers, name="new_week2",
                   description="Start a new challenge event! Weekly or Bingo")
@default_permissions(administrator=True)
async def new_week(ctx, game_mode):
    if default_permissions(administrator=True):
        if game_mode == "Weekly":
            await ctx.respond(f"Preparing new {game_mode} challenge.")
            # Function to move temp_weekly data to weekly, weekly_dim, score, and ???
            pause(1)
            await ctx.respond(f"Moving data from previous challenge into the ether.")
            # Function to determine the scores of each player this week.
            pause(1)
            await ctx.respond(f"Determining quasar phase shift physics.")
            # Function to drop rows in temp_weekly and start from scratch
            pause(1)
            await ctx.respond(f"New {game_mode} challenge is ready!")
        elif game_mode == "Bingo":
            await ctx.respond(f"Preparing new {game_mode} challenge.")
            # Function to move temp_bingo data to bingo, weekly_dim, score, and achievement
            pause(1)
            await ctx.respond(f"Dropping data from previous challenge into free fall.")
            # Function to determine the scores of each player this week.
            pause(1)
            await ctx.respond(f"Biscuits being counted.")
            # Function to drop rows in temp_bingo and start from scratch
            pause(1)
            await ctx.respond(f"New {game_mode} challenge is ready!")
        else:
            await ctx.respond(f"{game_mode} is not an existing mode. Please enter Standard or Bingo.")
    else:
        await ctx.respond(f"I'm sorry {ctx.author}, I can't let you do that.")


make_db()

bot.run(TOKEN)
