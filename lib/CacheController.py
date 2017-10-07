# CacheController.py
# included in ATP Probability
# by xavikortes 2017

cache = {}
matchScore = {}


def getCache(key):
    if key in cache:
        return cache[key]
    return -1


def getScore():
    return matchScore


def setCache(key, value):
    cache[key] = value


def setScore(bestOf=3, tiebreakerMatch=True, tiebreakerSet=True, tiebreakerGame=False, setsA=0, setsB=0, gamesA=0, gamesB=0, pointsA=0, pointsB=0, server="A"):
    matchScore["bO"] = bestOf
    matchScore["tbM"] = tiebreakerMatch
    matchScore["tbS"] = tiebreakerSet
    matchScore["tbG"] = tiebreakerGame
    matchScore["s"] = server
    matchScore["sA"] = setsA
    matchScore["sB"] = setsB
    matchScore["gA"] = gamesA
    matchScore["gB"] = gamesB
    matchScore["pA"] = pointsA
    matchScore["pB"] = pointsB


def clearCache():
    for c in list(cache.keys()):
        del cache[c]
    for s in list(matchScore.keys()):
        matchScore[s] = None
