import sqlite3
import random
from datetime import datetime as dt


class UsersDB:
    __instance = None

    @staticmethod
    def get_instance():
        if UsersDB.__instance is None:
            UsersDB()
        return UsersDB.__instance

    def __init__(self):
        if UsersDB.__instance is not None:
            raise Exception("You're doing it wrong, don't do it")
        else:
            self.con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
            self.init_db()
            UsersDB.__instance = self

    def init_db(self):
        with self.con:
            cur = self.con.cursor()
            cur.execute(
                "CREATE TABLE Users(Id INTEGER PRIMARY_KEY, username TEXT, last_seen timestamp)"
            )
            n = dt.now()
            for i, (u, t) in enumerate(
                    [
                        ("sergei", n.replace(month=8, day=3)),
                        ("valentin87", n.replace(month=8, day=4)),
                        ("igor99", n.replace(month=7, day=1)),
                        ("anton4", n.replace(month=1, day=10)),
                        ("vera2000", n.replace(month=4, day=14)),
                        ("sunnyside", n.replace(month=2, day=24)),
                        ("sarah.connor", n.replace(month=1, day=2)),
                        ("andrey3", n.replace(month=4, day=21)),
                        ("alexei22", n.replace(month=2, day=17)),

                    ],
                    start=100,
            ):
                h = random.randrange(0, 24)
                m = random.randrange(0, 60)
                s = random.randrange(0, 60)
                us = random.randrange(0, 1000000)
                t = t.replace(hour=h, minute=m, second=s, microsecond=us)
                cur.execute("INSERT INTO Users values(?, ?, ?)", (i, u, t))


def list_users():
    users = UsersDB.get_instance()
    known_users = []
    with users.con:
        cur = users.con.cursor()
        cur.execute("SELECT username, last_seen FROM Users")
        known_users = cur.fetchall()
    return known_users  # [(u, t) for _, u, t in known_users]


def query_user_last_seen(username):
    users = UsersDB.get_instance()
    with users.con:
        cur = users.con.cursor()
        cur.execute("SELECT last_seen FROM Users where username=?", (username,))
        results = cur.fetchone()
    return results[0] if (results and len(results) > 0) else dt.now()
