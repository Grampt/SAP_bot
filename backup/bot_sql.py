import numpy as np
import sqlite3
from weeklySQL import weeklySQL

con = sqlite3.connect(':memory')

c = con.cursor()

c.execute("""CREATE TABLE weekly (
                date text,
                user_id text,
                pt_standard integer,
                pt_hard integer,
                pt_reverse integer,
                pt_perfect integer,
                pt_sloth integer,
                pt_food integer,
                pt_level integer,
                pt_extreme integer
                )""")


def input_weekly_standard(w_in):
    with con:
        c.execute("INSERT INTO weekly VALUES (:date, :user_id, :pt_standard",
                  {'date': w_in.date, 'user_id': w_in.user_id, "pt_standard": w_in.pt_standard})


def input_weekly_hard(w_in):
    with con:
        c.execute("INSERT INTO weekly VALUES (:date, :user_id, :pt_hard",
                  {'date': w_in.date, 'user_id': w_in.user_id, "pt_hard": w_in.pt_hard})


def input_weekly_reverse(w_in):
    with con:
        c.execute("INSERT INTO weekly VALUES (:date, :user_id, :pt_reverse",
                  {'date': w_in.date, 'user_id': w_in.user_id, "pt_reverse": w_in.pt_reverse})


def input_weekly_perfect(w_in):
    with con:
        c.execute("INSERT INTO weekly VALUES (:date, :user_id, :pt_perfect",
                  {'date': w_in.date, 'user_id': w_in.user_id, "pt_perfect": w_in.pt_perfect})


def input_weekly_sloth(w_in):
    with con:
        c.execute("INSERT INTO weekly VALUES (:date, :user_id, :pt_sloth",
                  {'date': w_in.date, 'user_id': w_in.user_id, "pt_sloth": w_in.pt_sloth})


def input_weekly_food(w_in):
    with con:
        c.execute("INSERT INTO weekly VALUES (:date, :user_id, :pt_food",
                  {'date': w_in.date, 'user_id': w_in.user_id, "pt_food": w_in.pt_food})


def input_weekly_level(w_in):
    with con:
        c.execute("INSERT INTO weekly VALUES (:date, :user_id, :pt_level",
                  {'date': w_in.date, 'user_id': w_in.user_id, "pt_level": w_in.pt_level})


def input_weekly_extreme(w_in):
    with con:
        c.execute("INSERT INTO weekly VALUES (:date, :user_id, :pt_extreme",
                  {'date': w_in.date, 'user_id': w_in.user_id, "pt_extreme": w_in.pt_extreme})
