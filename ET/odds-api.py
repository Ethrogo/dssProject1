import requests, urllib
from datetime import datetime
import mysql
import mysql.connector
import pandas as pd


BASE_URL = 'https://api.prop-odds.com'
API_KEY = 'EEB8rCEAmAl6vHGoeLy9Z6LLCXRLSqTTuUGkc4MCXw'

def get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

    print('Request failed with status:', response.status_code)
    return {}

def get_nba_games():
    now = datetime.now()
    query_params = {
        'date': now.strftime('%Y-%m-%d'),
        'tz': 'America/New_York',
        'api_key': API_KEY,
    }
    params = urllib.parse.urlencode(query_params)
    url = BASE_URL + '/beta/games/nba?' + params
    return get_request(url)

def get_game_info(game_id):
    query_params = {
        'api_key': API_KEY,
    }
    params = urllib.parse.urlencode(query_params)
    url = BASE_URL + '/beta/game/' + game_id + '?' + params
    return get_request(url)

def get_markets(game_id):
    query_params = {
        'api_key': API_KEY,
    }
    params = urllib.parse.urlencode(query_params)
    url = BASE_URL + '/beta/markets/' + game_id + '?' + params
    return get_request(url)

def get_most_recent_odds(game_id, market):
    query_params = {
        'api_key': API_KEY,
    }
    params = urllib.parse.urlencode(query_params)
    url = BASE_URL + '/beta/odds/' + game_id + '/' + market + '?' + params
    return get_request(url)

def get_team_id(sql_cur, name):
    quer_str = "SELECT id FROM Teams WHERE name = '" + name + "'"
    try: 
        sql_cur.execute(quer_str)
        return sql_cur.fetchall()[0][0]
    except: 
        return -1

sql_con = mysql.connector.connect(host="localhost", user="root", password="Elephant123!")
sql_cur = sql_con.cursor(buffered=True)
sql_cur.execute("USE sportsDB")
games = get_nba_games()

index = 0
for game in games['games']:
    home_id = get_team_id(sql_cur=sql_cur, name=game['home_team'].strip())
    away_id = get_team_id(sql_cur=sql_cur, name=game['away_team'].strip())
    game_id = game['game_id']
    try: 
        odds = get_most_recent_odds(game_id, 'moneyline')
        away_odds = odds['sportsbooks'][0]['market']['outcomes'][0]['odds']
        home_odds = odds['sportsbooks'][0]['market']['outcomes'][1]['odds']
        sql_insert = "INSERT INTO FutureOdds (id, home_team_id, away_team_id, home_team_ml_odds, away_team_ml_odds) VALUES (%s, %s, %s, %s, %s)"
        sql_cur.execute(sql_insert, (index, home_id, away_id, home_odds, away_odds))
    except:
        print("fail")
        
    index += 1
    
sql_con.commit()
sql_cur.close()
sql_con.close()

    