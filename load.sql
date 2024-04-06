/** Find the number of wins from the team with id = 16 in the GameArchives **/
SELECT COUNT(*) AS total_wins
FROM GameArchives
WHERE
    (home_team_id = 16 AND home_team_score > away_team_score)
    OR
    (away_team_id = 16 AND away_team_score > home_team_score);


/** If the lakers have a upcomming game, Find their odds and opponents odds **/
SELECT
    Teams.name AS HomeTeam,
    Teams_Away.name AS AwayTeam,
    FutureOdds.Home_team_ml_odds AS HomeTeamOdds,
    FutureOdds.Away_team_ml_odds AS AwayTeamOdds
FROM
    FutureOdds
JOIN
    Teams ON FutureOdds.home_team_id = Teams.id
JOIN
    Teams AS Teams_Away ON FutureOdds.away_team_id = Teams_Away.id
WHERE
    (Teams.name = 'Los Angeles Lakers' OR Teams_Away.name = 'Los Angeles Lakers');

/** Selects all of the active basketball players (as of 2018) **/
SELECT Players.name
FROM Players
INNER JOIN Sports ON Players.sport_id = Sports.id
WHERE Sports.name = 'Basketball' AND Players.Is_active = true;