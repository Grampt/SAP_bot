import discord
import sqlite3
import numpy as np
from discord import option
import env
import datetime
import turtle
from weeklySQL import WeeklySQL

TOKEN = env.token
testingServers = env.serverList
bot = discord.Bot()

con = sqlite3.connect(':memory:')

c = con.cursor()

weekly_id_current = 0
challenge_type = "weekly"
current_weekly_date = '2023-04-28 09:55:20.156'


def checktablexists(dbcon, tablename):
    """Checks to see if the database already exists"""
    dbcurs = dbcon.cursor()
    dbcurs.execute("""SELECT name FROM sqlite_master WHERE type ='table'""")
    print(dbcurs.fetchall())
    if dbcurs.fetchone() is None :
        dbcurs.close()
#        return True
    else:
        dbcurs.close()
#        return False


def make_db():
    # "Make the weekly tables"
    if checktablexists(con, "weekly"):
        print("weekly exists")
        return
    else:
        c.execute("""CREATE TABLE weekly (
                        compound_id text NOT NULL,
                        user_id text,
                        weekly_id integer,
                        mode integer,
                        score integer,
                        date_entered text,
                        PRIMARY KEY(compound_id, weekly_id, mode)
                        )""")
        print("weekly created")
    if checktablexists(con, "temp_weekly"):
        print("temp_weekly exists")
        return
    else:
        c.execute("""CREATE TABLE temp_weekly (
                        compound_id text NOT NULL,
                        user_id text,
                        weekly_id integer,
                        mode integer,
                        score integer,
                        date_entered text,
                        PRIMARY KEY(compound_id, weekly_id, mode)
                        )""")
        print("temp_weekly created")
    # "Make the bingo tables"
    if checktablexists(con, "bingo"):
        print("bingo exists")
        return
    else:
        c.execute("""CREATE TABLE bingo (
                        compound_id text NOT NULL,
                        user_id text,
                        weekly_id integer,
                        achievement integer,
                        ranking integer,
                        score integer,
                        date_entered text,
                        PRIMARY KEY(weekly_id, achievement, ranking)
                        )""")
        print("bingo created")
    if checktablexists(con, "temp_bingo"):
        print("temp_bingo exists")
        return
    else:
        c.execute("""CREATE TABLE temp_bingo (
                        compound_id text NOT NULL,
                        user_id text,
                        weekly_id integer,
                        achievement integer,
                        ranking integer,
                        score integer,
                        date_entered text,
                        PRIMARY KEY(weekly_id, achievement, ranking)
                        )""")
        print("temp_bingo created")
    # "Make the auxiliary tables"
    if checktablexists(con, "score"):
        print("score exists")
        return
    else:
        c.execute("""CREATE TABLE score (
                        user_id text,
                        date text NOT NULL,
                        score integer,
                        PRIMARY KEY(user_id)
                        )""")
        print("score created")
    if checktablexists(con, "mode_dim"):
        print("mode_dim exists")
        return
    else:
        c.execute("""CREATE TABLE mode_dim (
                        mode integer,
                        description text,
                        PRIMARY KEY(mode)
                        )""")
        print("mode_dim created")
    if checktablexists(con, "week_dim"):
        print("week_dim exists")
        return
    else:
        c.execute("""CREATE TABLE week_dim (
                        weekly_id integer,
                        date text,
                        PRIMARY KEY(weekly_id)
                        )""")
        print("mode_dim created")


def input_temp_weekly(w_in):

    user_id = w_in[1]
    entry_date = w_in[6]
    mode = w_in[7]

    def scorer(var):
        match var:
            case 1:
                return 2
            case 2:
                return 1
            case 3:
                return 2
            case 4:
                return 1
            case 5:
                return 2
            case 6:
                return 1
            case 7:
                return 2
            case 8:
                return 2

    points = scorer(mode)
    compound = str(user_id) + '*' + str(weekly_id_current)

    with con:
        c.execute("INSERT INTO temp_weekly VALUES (:compound_id, :user_id, :weekly_id, :mode,"
                  " :score, :date_entered)",
                  {'compound_id': compound, 'user_id': user_id, 'weekly_id': weekly_id_current, 'mode': mode,
                   'score': points, 'date_entered': entry_date})


def get_game_attr(ctx, mode_num):
    author_name = ctx.user
    author_id = ctx.user.id
    guild = ctx.guild
    guild_id = ctx.guild.id
    current_weekly = current_weekly_date
    weekly_id = weekly_id_current
    entry_date = datetime.datetime.now()
    mode = mode_num
    return [author_name, author_id, guild, guild_id, current_weekly, weekly_id, entry_date, mode]


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
    print(get_table_data(con, challenge_type, ctx))


@bot.slash_command(guild_ids=testingServers, name="weekly", description="Claim a weekly win")
async def work(ctx, mode):
    await ctx.respond(f"You claimed the blank mode!")
    input_temp_weekly(get_game_attr(ctx, mode))

"""
@bot.slash_command(name="sum", description="Add stuff")
async def add(ctx, first: int, second: int):
    plus = first + second
    await ctx.respond(f"{first} plus {second} is {plus}.")


@bot.slash_command(name="dif", description="Subtract stuff")
async def subtract(ctx, first: int, second: int):
    dif = first - second
    await ctx.respond(f"{first} minus {second} is {dif}.")
"""

make_db()

bot.run(TOKEN)