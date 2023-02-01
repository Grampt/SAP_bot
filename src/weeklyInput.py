import numpy as np
import sqlite3
from weeklySQL import WeeklySQL
from weeklySQL import WeeklyInput

con = sqlite3.connect(':memory:')

c = con.cursor()

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

current_id = 0
current_date = '2023-04-06 11:23:32.156'


def input_weekly_standard(w_in):
    global current_id
    global current_date

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
    compound = str(w_in.user_id + '*' + current_date)

    with con:
        c.execute("INSERT INTO weekly VALUES (:compound_id, :user_id, :date, :weekly_id, :mode, :score, :date_entered)",
                  {'compound_id': compound, 'user_id': w_in.user_id, 'date': current_date,
                   'weekly_id': current_id, 'mode': w_in.mode, 'score': points, 'date_entered': w_in.date_entered})


def get_user_by_id(user_id):
    c.execute("SELECT * FROM weekly WHERE user_id=:user_id", {'user_id': user_id})
    return c.fetchall()


def get_user_by_score(score):
    c.execute("SELECT * FROM weekly WHERE score=:score", {'score': score})
    return c.fetchall()


week1 = WeeklySQL('Jenny', 4, '2023-04-28 09:55:20.156')
week2 = WeeklySQL('Greg', 3, '2023-04-21 09:40:32.156')

input_weekly_standard(week1)
input_weekly_standard(week2)

users = get_user_by_id('Jenny')
print(users)

users = get_user_by_score(2)
print(users)
