import mysql
import mysql.connector
from  mysql.connector.errors import *


def create_tables(cursor): 
    try: 
        cursor.execute("CREATE TABLE Sports (id INT AUTO_INCREMENT PRIMARY KEY,  name  VARCHAR(63))")
        cursor.execute("INSERT INTO Sports VALUES (0, 'Basketball')")
    except: 
        pass
    try: 
        cursor.execute("CREATE TABLE Teams (id INT AUTO_INCREMENT PRIMARY KEY, sport_id int, FOREIGN KEY (sport_id) REFERENCES Sports(id), name VARCHAR(63), UNIQUE(name), abbr VARCHAR(3), UNIQUE(abbr))")
    except: 
        pass
    try: 
        cursor.execute("CREATE TABLE Players (id INT PRIMARY KEY,  name  VARCHAR(63), is_active BOOL, sport_id int, FOREIGN KEY (sport_id) REFERENCES Sports(id))")
    except: 
        pass
    try: 
        cursor.execute("CREATE TABLE GameArchives (id INT PRIMARY KEY,  home_team_id  INT, Foreign Key (home_team_id) REFERENCES Teams(id), away_team_id  INT, Foreign Key (away_team_id) REFERENCES Teams(id), home_team_score INT, away_team_score INT, game_date DATE)")
    except: 
        pass
    try: 
        cursor.execute("CREATE TABLE FutureOdds (id INT PRIMARY KEY,  home_team_id  INT, Foreign Key (home_team_id) REFERENCES Teams(id), away_team_id  INT, Foreign Key (away_team_id) REFERENCES Teams(id), home_team_ml_odds VARCHAR(15), away_team_ml_odds VARCHAR(15))")
    except: 
        pass
    
    

con = mysql.connector.connect(host="localhost", user="root", password="Elephant123!")
cursor = con.cursor()
try: 
    cursor.execute("CREATE DATABASE sportsDB")
except DatabaseError as e: 
    pass


cursor.execute("USE sportsDB")
create_tables(cursor=cursor)
cursor.close()
con.close()