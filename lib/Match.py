# Match.py
# included in ATP Probability
# by xavikortes 2017

from lib import CacheController
from lib import Server
from lib import Set


def getKey(type, pointsA, pointsB, gamesA, gamesB, setsA, setsB, bestOf, tiebreaker):
    return "Match__" + type + "__" + str(pointsA) + "__" + str(pointsB) + "__" + str(gamesA) + "__" + str(gamesB) + "__" + str(setsA) + "__" + str(setsB) + "__" + str(bestOf) + "__" + str(tiebreaker)


def probability(bestOf, tiebreaker, setsA=0, setsB=0, gamesA=0, gamesB=0, pointsA=0, pointsB=0):
    setProb = Set.probability(True, Server.arbitrary(), gamesA, gamesB, pointsA, pointsB)
    key = getKey("prob", pointsA, pointsB, gamesA, gamesB, setsA, setsB, bestOf, tiebreaker)

    prob = CacheController.getCache(key)
    if prob == -1:
        if setsA == 3 and setsB <= 2 and bestOf == 5:
            prob = 1
        elif setsA == 2 and setsB <= 1 and bestOf == 3:
            prob = 1
        elif setsB == 3 and setsA <= 2 and bestOf == 5:
            prob = 0
        elif setsB == 2 and setsA <= 1 and bestOf == 3:
            prob = 0
        elif (setsA == 2 and setsB == 2 and bestOf == 5) or (setsA == 1 and setsB == 1 and bestOf == 3) and tiebreaker:
            prob = setProb
        elif (setsA == 2 and setsB == 2 and bestOf == 5) or (setsA == 1 and setsB == 1 and bestOf == 3) and not tiebreaker:
            prob = Set.probability(False, Server.arbitrary(), gamesA, gamesB, pointsA, pointsB)
        else:
            prob = setProb * probability(bestOf, tiebreaker, setsA + 1, setsB) + (1 - setProb) * probability(bestOf, tiebreaker, setsA, setsB + 1)

        CacheController.setCache(key, prob)

    return prob


def numberOfPoints(bestOf, tiebreaker, setsA=0, setsB=0, gamesA=0, gamesB=0, pointsA=0, pointsB=0):
    key = getKey("points", pointsA, pointsB, gamesA, gamesB, setsA, setsB, bestOf, tiebreaker)

    points = CacheController.getCache(key)
    if points == -1:
        points = numberOfSets(bestOf, tiebreaker, setsA, setsB, gamesA, gamesB, pointsA, pointsB) * Set.numberOfPoints(True, Server.arbitrary(), gamesA, gamesB, pointsA, pointsB)
        CacheController.setCache(key, points)

    return points


def numberOfGames(bestOf, tiebreaker, setsA=0, setsB=0, gamesA=0, gamesB=0, pointsA=0, pointsB=0):
    key = getKey("games", pointsA, pointsB, gamesA, gamesB, setsA, setsB, bestOf, tiebreaker)

    games = CacheController.getCache(key)
    if games == -1:
        games = numberOfSets(bestOf, tiebreaker, setsA, setsB, gamesA, gamesB, pointsA, pointsB) * Set.numberOfGames(True, Server.arbitrary(), gamesA, gamesB, pointsA, pointsB)
        CacheController.setCache(key, games)

    return games


def numberOfSets(bestOf, tiebreaker, setsA=0, setsB=0, gamesA=0, gamesB=0, pointsA=0, pointsB=0):
    setProb = Set.probability(tiebreaker, Server.arbitrary(), gamesA, gamesB, pointsA, pointsB)
    key = getKey("sets", pointsA, pointsB, gamesA, gamesB, setsA, setsB, bestOf, tiebreaker)

    sets = CacheController.getCache(key)
    if sets == -1:
        if setsA == 3 and setsB <= 2 and bestOf == 5:
            sets = 0
        elif setsA == 2 and setsB <= 1 and bestOf == 3:
            sets = 0
        elif setsB == 3 and setsA <= 2 and bestOf == 5:
            sets = 0
        elif setsB == 2 and setsA <= 1 and bestOf == 3:
            sets = 0
        elif (setsA == 2 and setsB == 2 and bestOf == 5) or (setsA == 1 and setsB == 1 and bestOf == 3):
            sets = 1
        else:
            sets = 1 + setProb * numberOfSets(bestOf, tiebreaker, setsA + 1, setsB) + (1 - setProb) * numberOfSets(bestOf, tiebreaker, setsA, setsB + 1)
        CacheController.setCache(key, sets)

    return sets
