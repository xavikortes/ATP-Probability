# Point.py
# included in ATP Probability
# by xavikortes 2017

from lib import CacheController
from lib import Server


# Pasar a setCache de CacheController
def updateCache(serveA, serveB):
    CacheController.setCache("Point__prob__A", serveA)
    CacheController.setCache("Point__prob__B", serveB)


def getKey(type, server):
    return "Point__" + type + "__" + str(server)


def probability(server):
    key = getKey("prob", Server.keep(server))

    prob = CacheController.getCache(key)
    if prob == -1:
        prob = 0.0
        CacheController.setCache(key, prob)

    return prob
