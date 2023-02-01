import discord
import sqlite3
import numpy as np
from discord import option
import env
import turtle
from weeklySQL import WeeklySQL

TOKEN = env.token
testingServers = env.serverList
bot = discord.Bot()

con = sqlite3.connect(':memory:')

c = con.cursor()

weekly_id_current = 0
current_weekly_date = '2023-04-28 09:55:20.156'


def checktablexists(dbcon, tablename):
    """Checks to see if the database already exists"""
    dbcurs = dbcon.cursor()
    dbcurs.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """, format(tablename.replace('\'', '\'\'')))
    if dbcurs.fetchone()[0] == 1:
        dbcurs.close()
        return True

    dbcurs.close()
    return False


def make_db():
    if checktablexists(c, "weekly"):
        return
    else:
        c.execute("""CREATE TABLE weekly (
                        compound_id text NOT NULL,
                        user_id text,
                        date text NOT NULL,
                        weekly_id integer,
                        mode integer,
                        score integer,
                        date_entered text,
                        PRIMARY KEY(compound_id, mode)
                        )""")


def input_weekly_standard(w_in):
    global weekly_id_current
    global current_weekly_date

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

    points = scorer(w_in.mode)
    compound = str(w_in.user_id + '*' + current_weekly_date)

    with con:
        c.execute("INSERT INTO weekly VALUES (:compound_id, :user_id, :date, :weekly_id, :mode, :score, :date_entered)",
                  {'compound_id': compound, 'user_id': w_in.user_id, 'date': current_weekly_date,
                   'weekly_id': weekly_id_current, 'mode': w_in.mode, 'score': points, 'date_entered': w_in.date_entered})


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


@bot.slash_command(guild_ids=testingServers, name="weekly", description="Claim a weekly win")
async def work(ctx, first: int):

    await ctx.respond(f"I am working! \n\nLatency: {bot.latency * 1000} ms.")


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

bot.run(TOKEN)
