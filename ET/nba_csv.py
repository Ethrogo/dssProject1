import mysql
import mysql.connector
import pandas as pd


sql_con = mysql.connector.connect(host="localhost", user="root", password="Elephant123!")
sql_cur = sql_con.cursor(buffered=True)
sql_cur.execute("USE sportsDB")

with open ("NBA-playerlist.csv") as f: 
    df = pd.read_csv(f)

index = 1
for row in df.iterrows():
    name = row[1]['DISPLAY_FIRST_LAST']
    year = row[1]['TO_YEAR']
    is_active = False
    if year == 2018: 
        is_active = True
    sql_cur.execute("INSERT INTO Players (id, name, is_active, sport_id) VALUES (%s, %s, %s, %s)", (index, name, is_active, 1))
    index += 1
sql_con.commit()
sql_cur.close()
sql_con.close()
    