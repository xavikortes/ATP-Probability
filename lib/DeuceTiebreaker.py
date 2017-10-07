# DeuceTiebreaker.py
# included in ATP Probability
# by xavikortes 2017

from lib import CacheController
from lib import Server
from lib import Point


def getKey(type, serveA, serveB, server):
    return "DeuceTiebreaker__" + type + "__" + str(serveA) + "__" + str(serveB) + "__" + str(server)


def probability(server):
    serveA = Point.probability(Server.keep(server))
    serveB = Point.probability(Server.change(server))
    key = getKey("prob", serveA, serveB, Server.keep(server))

    prob = CacheController.getCache(key)
    if prob == -1:
        prob = (serveA * (1 - serveB)) / ((serveA * (1 - serveB)) + ((1 - serveA) * serveB))

        if Server.keep(server) != "A":
            prob = 1 - prob

        CacheController.setCache(key, prob)

    return prob


def numberOfPoints(server):
    serveA = Point.probability(Server.keep(server))
    serveB = Point.probability(Server.change(server))
    key = getKey("points", serveA, serveB, Server.keep(server))

    points = CacheController.getCache(key)
    if points == -1:
        points = 2 / (serveA * (1 - serveB) + (1 - serveA) * serveB)
        CacheController.setCache(key, points)

    return points
