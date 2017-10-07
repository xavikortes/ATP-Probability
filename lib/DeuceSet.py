# DeuceSet.py
# included in ATP Probability
# by xavikortes 2017

from lib import CacheController
from lib import Server
from lib import Game


def getKey(type, gameA, gameB, server):
    return "DeuceSet__" + type + "__" + str(gameA) + "__" + str(gameB) + "__" + str(server)


def probability(server):
    gameA = Game.probability(Server.keep(server))
    gameB = Game.probability(Server.change(server))
    key = getKey("prob", gameA, gameB, Server.keep(server))

    prob = CacheController.getCache(key)
    if prob == -1:
        prob = (gameA * (1 - gameB)) / (gameA * (1 - gameB) + (1 - gameA) * gameB)
        CacheController.setCache(key, prob)

    return prob


def numberOfPoints(server):
    gameA = Game.probability(Server.keep(server))
    gameB = Game.probability(Server.change(server))
    key = getKey("points", gameA, gameB, Server.keep(server))

    points = CacheController.getCache(key)
    if points == -1:
        points = numberOfGames(server) * Game.numberOfPoints(server, 0, 0)
        CacheController.setCache(key, points)

    return points


def numberOfGames(server):
    gameA = Game.probability(Server.keep(server))
    gameB = Game.probability(Server.change(server))
    key = getKey("games", gameA, gameB, Server.keep(server))

    games = CacheController.getCache(key)
    if games == -1:
        games = 2 / (gameA * (1 - gameB) + (1 - gameA) * gameB)

        if Server.keep(server) != "A":
            games = 1 - games

        CacheController.setCache(key, games)

    return games
