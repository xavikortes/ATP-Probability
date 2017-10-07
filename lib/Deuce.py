# Deuce.py
# included in ATP Probability
# by xavikortes 2017

from lib import CacheController
from lib import Server
from lib import Point


def getKey(type, pointProb):
    return "Deuce__" + type + "__" + str(pointProb)


def probability(server):
    pointProb = Point.probability(Server.keep(server))
    key = getKey("prob", pointProb)

    prob = CacheController.getCache(key)
    if prob == -1:
        prob = (pointProb * pointProb) / (pointProb * pointProb + (1 - pointProb) * (1 - pointProb))
        CacheController.setCache(key, prob)

    return prob


def numberOfPoints(server):
    pointProb = Point.probability(Server.keep(server))
    key = getKey("points", pointProb)

    points = CacheController.getCache(key)
    if points == -1:
        points = 2 / (pointProb * pointProb + (1 - pointProb) * (1 - pointProb))

        if Server.keep(server) != "A":
            points = 1 - points

        CacheController.setCache(key, points)

    return points
