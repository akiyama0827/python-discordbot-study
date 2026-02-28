CREATE TABLE IF NOT EXISTS player (
    user_id INTEGER PRIMARY KEY,
    enlistment_date TEXT,
    discharge_date TEXT,
    branch TEXT
);

CREATE TABLE IF NOT EXISTS guild (
    guild_id INTEGER PRIMARY KEY,
    ohaasa_channel INTEGER,
    celebrate_channel INTEGER
)