# Main.py
# included in ATP Probability
# by xavikortes 2017

from lib import CacheController
from lib import Point
from lib import Game
from lib import GameTiebreaker
from lib import Set
from lib import Match


def setPlayersAverage(avgP1=0.5, avgP2=0.5):
    CacheController.clearCache()
    CacheController.setCache("Point__prob__A", avgP1)
    CacheController.setCache("Point__prob__B", avgP2)


def setScore(bestOf=3, tiebreakerMatch=False, setsA=0, setsB=0, gamesA=0, gamesB=0, pointsA=0, pointsB=0, server="A"):
    tiebreakerSet = True
    if (bestOf == 3 and setsA == setsB and setsA == 1 and not tiebreakerMatch) or (bestOf == 5 and setsA == setsB and setsA == 2 and not tiebreakerMatch):
        tiebreakerSet = False
    tiebreakerGame = False
    if gamesA == gamesB and gamesA == 6 and tiebreakerSet:
        tiebreakerGame = True
    CacheController.setScore(bestOf, tiebreakerMatch, tiebreakerSet, tiebreakerGame, setsA, setsB, gamesA, gamesB, pointsA, pointsB, server)


def getProbability(mode="winMatch"):
    s = CacheController.getScore()

    if mode == "winMatch":
        return Match.probability(s["bO"], s["tbM"], s["sA"], s["sB"], s["gA"], s["gB"], s["pA"], s["pB"])
    elif mode == "winSet":
        return Set.probability(s["tbS"], s["s"], s["gA"], s["gB"], s["pA"], s["pB"])
    elif mode == "winGame":
        if s["tbG"]:
            return GameTiebreaker.probability(s["s"], s["pA"], s["pB"])
        else:
            return Game.probability(s["s"], s["pA"], s["pB"])
    elif mode == "winPoint":
        return Point.probability(s["s"])
    elif mode == "setsInMatch":
        return Match.sets(s["bO"], s["tbM"], s["sA"], s["sB"], s["gA"], s["gB"], s["pA"], s["pB"])
    elif mode == "gamesInMatch":
        return Match.games(s["bO"], s["tbM"], s["sA"], s["sB"], s["gA"], s["gB"], s["pA"], s["pB"])
    elif mode == "gamesInSet":
        return Set.games(s["tbS"], s["s"], s["gA"], s["gB"], s["pA"], s["pB"])
    elif mode == "pointsInMatch":
        return Match.points(s["bO"], s["tbM"], s["sA"], s["sB"], s["gA"], s["gB"], s["pA"], s["pB"])
    elif mode == "pointsInSet":
        return Set.points(s["tbS"], s["s"], s["gA"], s["gB"], s["pA"], s["pB"])
    elif mode == "pointsInGame":
        if s["tbG"]:
            return GameTiebreaker.points(s["s"], s["pA"], s["pB"])
        else:
            return Game.points(s["s"], s["pA"], s["pB"])
    else:
        return False
