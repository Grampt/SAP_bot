import sqlite3

con = sqlite3.connect(':memory:')

c = con.cursor()


class WeeklySQL:
    """Write the completed data for the current weekly challenge"""

    def __init__(self, user_id, mode, date_entered):
        self.user_id = user_id
        self.mode = mode
        self.date_entered = date_entered

    def __repr__(self):
        return "User('{}', '{}', '{}')".format(self.user_id, self.mode, self.date_entered)


class WeeklyInput:

    def __init__(self, user_id, entry_date, mode):
        self.user_id = user_id
        self.entry_date = entry_date
        self.mode = mode

    def __repr__(self):
        return "User('{}', '{}', '{}')".format(self.user_id, self.mode, self.date_entered)

    def input_temp_weekly(w_in, conn, weekly_id_current):

        user_id = w_in[1]
        server_id = w_in[3]
        entry_date = w_in[5]
        mode = w_in[6]

        temp_con = conn
        temp_curs = temp_con.cursor()

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

        with temp_con:
            try:
                temp_curs.execute("INSERT INTO temp_weekly VALUES (:compound_id, :user_id, :weekly_id, :mode,"
                              " :score, :server_id, :entry_date)",
                              {'compound_id': compound, 'user_id': user_id, 'weekly_id': weekly_id_current,
                               'mode': mode, 'score': points, 'server_id': server_id, 'entry_date': entry_date})
                temp_con.commit()
            except sqlite3.IntegrityError as e:
                print("You cannot claim the same challenge this week.", e)
                return
