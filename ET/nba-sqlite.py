import sqlite3
import mysql
import mysql.connector

def add_team_names(cursor, sql_cur, sql_con):
    all_teams = cursor.execute("SELECT full_name FROM team")
    names = all_teams.fetchall()
    i = 1
    for name in names: 
        try: 
            sql_insert = "INSERT INTO Teams (id, sport_id, name) VALUES (%s, %s, %s)"
            val = (str(i), "1", name[0])
            sql_cur.execute(sql_insert, val)
        except: 
            print("fail")
        i += 1
    sql_con.commit()
    
con = sqlite3.connect("nba.sqlite")
cursor = con.cursor()

sql_con = mysql.connector.connect(host="localhost", user="root", password="Elephant123!")
sql_cur = sql_con.cursor()
sql_cur.execute("USE sportsDB")

add_team_names(cursor=cursor, sql_cur=sql_cur)




