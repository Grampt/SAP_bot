import sqlite3


class WeeklySQL:
    """Write the completed data for the current weekly challenge"""

    con = sqlite3.connect(':memory:')

    c = con.cursor()

    def __init__(self, user_id, mode, date_entered):
        self.user_id = user_id
        self.mode = mode
        self.date_entered = date_entered

    def __repr__(self):
        return "User('{}', '{}', '{}')".format(self.user_id, self.mode, self.date_entered)


class WeeklyInput:

    def input_weekly_standard(self, var_in, con, c, week_id, week_date):
        current_id = week_id
        current_date = week_date


        def scorer(mode):
            match mode:
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

        points = scorer(var_in.mode)
        compound = str(var_in.user_id + '*' + current_date)

        with con:
            c.execute(
                "INSERT INTO weekly VALUES (:compound_id, :user_id, :date, :weekly_id, :mode, :score, :date_entered)",
                {'compound_id': compound, 'user_id': var_in.user_id, 'date': current_date,
                 'weekly_id': current_id, 'mode': var_in.mode, 'score': points, 'date_entered': var_in.date_entered})
