import sqlite3
import datetime
import time


database = ':memory:'

tables = ['temp_weekly', 'weekly', 'temp_bingo', 'bingo', 'score', 'mode_dim', 'week_dim', 'achievement_dim',
          'img_dim', 'team_achieve_dim']


def create_connection(db_file):
    connect = None
    try:
        connect = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return connect


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

