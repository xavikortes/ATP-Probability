# example.py
# included in ATP Probability
# by xavikortes 2017

from lib import Main

# Sets the players average probability of winning a point at service
# It can be calculated by service winning % or by service winning % vs opponent's return winning %
Main.setPlayersAverage(0.62, 0.60)

# Sets the current score of the match
# parameters (bestOf=3, tiebreaker=True, setsA=0, setsB=0, gamesA=0, gamesB=0, pointsA=0, pointsB=0, server="A")
# bestOf (3/5). Max number of sets to play in the match
# tiebreaker. True if in the last set, a tiebreaker is played at 6-6
# Other. Current score of sets, games and points for players A and B (points are displayed as 0,1,2,3..)
# server. Player who is currently server
Main.setScore(5, True, 1, 1, 5, 3, 1, 1, "A")

# Get the probability of winning a game, set, match or the number of points, games, and sets remaining
# parameters (mode)
# mode can be set with a value of the list:
# - winMatch
# - winSet
# - winGame
# - winPoint
# - pointsInMatch
# - pointsInSet
# - pointsInGame
# - gamesInMatch
# - gamesInSet
# - setsInMatch
print(Main.getProbability("winSet"))
