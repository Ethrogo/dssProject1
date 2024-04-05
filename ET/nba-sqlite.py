import sqlite3


con = sqlite3.connect("nba.sqlite")
cursor = con.cursor()
all_games = cursor.execute("SELECT team_name_home, team_name_away, game_id, wl_home, ")

