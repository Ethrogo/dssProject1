import sqlite3
import mysql
import mysql.connector

def get_team_id(sql_cur, abbr):
    quer_str = "SELECT id FROM Teams WHERE abbr = '" + abbr + "'"
    try: 
        sql_cur.execute(quer_str)
        
        return sql_cur.fetchall()[0][0]
    except: 
        #print(name)
        return -1
    
    
def add_team_names(cursor, sql_cur, sql_con):
    all_teams = cursor.execute("SELECT full_name, abbreviation FROM team")
    names = all_teams.fetchall()
    i = 1
    for name in names: 
        try: 
            sql_insert = "INSERT INTO Teams (id, sport_id, name, abbr) VALUES (%s, %s, %s, %s)"
            val = (str(i), "1", name[0], name[1])
            sql_cur.execute(sql_insert, val)
        except: 
            pass
        i += 1
    sql_con.commit()

def add_past_games(cursor, sql_cur, sql_con):
    all_games = cursor.execute("SELECT game_id, team_abbreviation_home, team_abbreviation_away, pts_home, pts_away, game_date FROM game")
    games = all_games.fetchall()
    
    for game in games: 
        try: 
            home_id = get_team_id(sql_cur, game[1])
            away_id = get_team_id(sql_cur, game[2])
            
            if home_id != -1 and away_id != -1:
                sql_insert = "INSERT INTO GameArchives (id, home_team_id, away_team_id, home_team_score, away_team_score, game_date) VALUES (%s, %s, %s, %s, %s, %s)"
                vals = (game[0], home_id, away_id, int(game[3]), int(game[4]), game[5])
                sql_cur.execute(sql_insert, vals)
        except: 
            pass
    sql_con.commit()
    
con = sqlite3.connect("nba.sqlite")
cursor = con.cursor()

sql_con = mysql.connector.connect(host="localhost", user="root", password="Elephant123!")
sql_cur = sql_con.cursor(buffered=True)
sql_cur.execute("USE sportsDB")

# add_team_names(cursor=cursor, sql_cur=sql_cur, sql_con=sql_con)
# add_past_games(cursor=cursor, sql_cur=sql_cur, sql_con=sql_con)
sql_cur.close()
cursor.close()