# Set.py
# included in ATP Probability
# by xavikortes 2017

from lib import CacheController
from lib import Server
from lib import Point
from lib import Game
from lib import GameTiebreaker
from lib import DeuceSet


def getKey(type, pointsA, pointsB, gamesA, gamesB, tiebreaker, pointProb, gameProb):
    return "Set__" + type + "__" + str(pointsA) + "__" + str(pointsB) + "__" + str(gamesA) + "__" + str(gamesB) + "__" + str(tiebreaker) + "__" + str(pointProb) + "__" + str(gameProb)


def probability(tiebreaker, server, gamesA=0, gamesB=0, pointsA=0, pointsB=0):
    pointProb = Point.probability(Server.keep(server))
    gameProb = Game.probability(Server.keep(server), pointsA, pointsB)
    key = getKey("prob", pointsA, pointsB, gamesA, gamesB, tiebreaker, pointProb, gameProb)

    prob = CacheController.getCache(key)
    if prob == -1:
        if (gamesA >= 6 and gamesB < (gamesA - 1)):
            prob = 1
        elif (gamesB >= 6 and gamesA < (gamesB - 1)):
            prob = 0
        elif gamesA == 6 and gamesB == 6 and tiebreaker:
            prob = GameTiebreaker.probability(Server.keep(server), pointsA, pointsB)
        elif gamesA == gamesB and gamesA >= 5 and not tiebreaker:
            prob = DeuceSet.probability(Server.keep(server))
        else:
            if Server.keep(server) == "A":
                prob = gameProb * probability(tiebreaker, Server.change(server), gamesA + 1, gamesB) + (1 - gameProb) * probability(tiebreaker, Server.change(server), gamesA, gamesB + 1)
            else:
                prob = gameProb * probability(tiebreaker, Server.change(server), gamesA, gamesB + 1) + (1 - gameProb) * probability(tiebreaker, Server.change(server), gamesA + 1, gamesB)

        CacheController.setCache(key, prob)

    return prob


def numberOfPoints(tiebreaker, server, gamesA=0, gamesB=0, pointsA=0, pointsB=0):
    pointProb = Point.probability(Server.keep(server))
    gameProb = Game.probability(Server.keep(server), pointsA, pointsB)
    key = getKey("points", pointsA, pointsB, gamesA, gamesB, tiebreaker, pointProb, gameProb)

    points = CacheController.getCache(key)
    if points == -1:
        points = numberOfGames(tiebreaker, server, gamesA, gamesB, pointsA, pointsB) * Game.numberOfPoints(server, pointsA, pointsB)
        CacheController.setCache(key, points)

    return points


def numberOfGames(tiebreaker, server, gamesA=0, gamesB=0, pointsA=0, pointsB=0):
    pointProb = Point.probability(Server.keep(server))
    gameProb = Game.probability(Server.keep(server), pointsA, pointsB)
    key = getKey("games", pointsA, pointsB, gamesA, gamesB, tiebreaker, pointProb, gameProb)

    games = CacheController.getCache(key)
    if games == -1:
        if (gamesA >= 6 and gamesB < (gamesA - 1)):
            games = 0
        elif (gamesB >= 6 and gamesA < (gamesB - 1)):
            games = 0
        elif gamesA == 6 and gamesB == 6 and tiebreaker:
            games = 1
        elif gamesA == gamesB and gamesA >= 5 and not tiebreaker:
            games = DeuceSet.numberOfGames(Server.keep(server))
        else:
            if Server.keep(server) == "A":
                games = 1 + gameProb * numberOfGames(tiebreaker, Server.change(server), gamesA + 1, gamesB) + (1 - gameProb) * numberOfGames(tiebreaker, Server.change(server), gamesA, gamesB + 1)
            else:
                games = 1 + gameProb * numberOfGames(tiebreaker, Server.change(server), gamesA, gamesB + 1) + (1 - gameProb) * numberOfGames(tiebreaker, Server.change(server), gamesA + 1, gamesB)

        CacheController.setCache(key, games)

    return games
