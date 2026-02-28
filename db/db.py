import sqlite3, os.path

DB_PATH = '/home/g02beonjjae02/python-discordbot-study/data/database.db'
BUILD_PATH = '/home/g02beonjjae02/python-discordbot-study/data/build.sql'

con = sqlite3.connect(DB_PATH)
cur = con.cursor()

def with_commit(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        commit()
        return result
    return inner

@with_commit
def build():
    if os.path.isfile(BUILD_PATH):
        scriptexec(BUILD_PATH)

def commit():
    con.commit()

def scriptexec(path):
    with open(path, 'r', encoding='utf-8') as script:
        cur.executescript(script.read())

@with_commit
def execute(command, values):
    cur.execute(command, values)
    return cur.rowcount

def field(command, *values):
    cur.execute(command, values)
    fetch = cur.fetchone()
    return fetch[0] if fetch else None

def record(command, *values):
    cur.execute(command, values)
    return cur.fetchone()

def recordAllItem(var_from, values):
    cur.execute(f"SELECT {values} FROM {var_from}")
    return cur.fetchall()