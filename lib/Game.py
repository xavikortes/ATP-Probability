# Game.py
# included in ATP Probability
# by xavikortes 2017

from lib import CacheController
from lib import Server
from lib import Point
from lib import Deuce


def getKey(type, pointsA, pointsB, pointProb):
    return "Game__" + type + "__" + str(pointsA) + "__" + str(pointsB) + "__" + str(pointProb)


def probability(server, pointsA=0, pointsB=0):
    pointProb = Point.probability(Server.keep(server))
    key = getKey("prob", pointsA, pointsB, pointProb)

    prob = CacheController.getCache(key)
    if prob == -1:
        if pointsA == 4 and pointsB <= 2:
            prob = 1
        elif pointsB == 4 and pointsA <= 2:
            prob = 0
        elif pointsA == 3 and pointsB == 3:
            prob = Deuce.probability(Server.keep(server))
        else:
            prob = pointProb * probability(Server.keep(server), pointsA + 1, pointsB) + (1 - pointProb) * probability(Server.keep(server), pointsA, pointsB + 1)

        CacheController.setCache(key, prob)

    return prob


def numberOfPoints(server, pointsA=0, pointsB=0):
    pointProb = Point.probability(Server.keep(server))
    key = getKey("points", pointsA, pointsB, pointProb)

    points = CacheController.getCache(key)
    if points == -1:
        if pointsA == 4 and pointsB <= 2:
            points = 0
        elif pointsB == 4 and pointsA <= 2:
            points = 0
        elif pointsA == 3 and pointsB == 3:
            points = Deuce.numberOfPoints(Server.keep(server))
        else:
            points = 1 + pointProb * numberOfPoints(Server.keep(server), pointsA + 1, pointsB) + (1 - pointProb) * numberOfPoints(Server.keep(server), pointsA, pointsB + 1)

        CacheController.setCache(key, points)

    return points
