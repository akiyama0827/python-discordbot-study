import sqlite3, os.path

DB_PATH = 'data/database.db'
BUILD_PATH = 'data/build.sql'

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