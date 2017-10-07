# GameTiebreaker.py
# included in ATP Probability
# by xavikortes 2017

from lib import CacheController
from lib import Server
from lib import Point
from lib import DeuceTiebreaker


def getKey(type, pointsA, pointsB, pointProb):
    return "GameTiebreaker__" + type + "__" + str(pointsA) + "__" + str(pointsB) + "__" + str(pointProb)


def probability(server, pointsA=0, pointsB=0):
    pointProb = Point.probability(Server.keep(server))
    key = getKey("prob", pointsA, pointsB, pointProb)

    prob = CacheController.getCache(key)
    if prob == -1:
        if pointsA == 7 and pointsB <= 5:
            prob = 1
        elif pointsB == 7 and pointsA <= 5:
            prob = 0
        elif pointsA == 6 and pointsB == 6:
            prob = DeuceTiebreaker.probability(Server.keep(server))
        elif ((pointsA + pointsB) % 2 == 0):
            if Server.keep(server) == "A":
                prob = pointProb * probability(Server.change(server), pointsA + 1, pointsB) + (1 - pointProb) * probability(Server.change(server), pointsA, pointsB + 1)
            else:
                prob = pointProb * probability(Server.change(server), pointsA, pointsB + 1) + (1 - pointProb) * probability(Server.change(server), pointsA + 1, pointsB)
        else:
            if Server.keep(server) == "A":
                prob = pointProb * probability(Server.keep(server), pointsA + 1, pointsB) + (1 - pointProb) * probability(Server.keep(server), pointsA, pointsB + 1)
            else:
                prob = pointProb * probability(Server.keep(server), pointsA, pointsB + 1) + (1 - pointProb) * probability(Server.keep(server), pointsA + 1, pointsB)

        CacheController.setCache(key, prob)

    return prob


def numberOfPoints(server, pointsA=0, pointsB=0):
    pointProb = Point.probability(Server.keep(server))
    key = getKey("points", pointsA, pointsB, pointProb)

    points = CacheController.getCache(key)
    if points == -1:
        if pointsA == 7 and pointsB <= 5:
            points = 0
        elif pointsB == 7 and pointsA <= 5:
            points = 0
        elif pointsA == 6 and pointsB == 6:
            points = DeuceTiebreaker.numberOfPoints(Server.keep(server))
        elif ((pointsA + pointsB) % 2 == 0):
            if Server.keep(server) == "A":
                points = 1 + pointProb * numberOfPoints(Server.change(server), pointsA + 1, pointsB) + (1 - pointProb) * numberOfPoints(Server.change(server), pointsA, pointsB + 1)
            else:
                points = 1 + pointProb * numberOfPoints(Server.change(server), pointsA, pointsB + 1) + (1 - pointProb) * numberOfPoints(Server.change(server), pointsA + 1, pointsB)
        else:
            if Server.keep(server) == "A":
                points = 1 + pointProb * numberOfPoints(Server.keep(server), pointsA + 1, pointsB) + (1 - pointProb) * numberOfPoints(Server.keep(server), pointsA, pointsB + 1)
            else:
                points = 1 + pointProb * numberOfPoints(Server.keep(server), pointsA, pointsB + 1) + (1 - pointProb) * numberOfPoints(Server.keep(server), pointsA + 1, pointsB)

        CacheController.setCache(key, points)

    return points
