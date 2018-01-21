# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 02:49:12 2017

@author: Reuben
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 17:38:01 2017

@author: Reuben
"""

#Simulation of monomono machine
import random
from itertools import accumulate
from collections import Counter
repeat = 0
coins = 0
lessen = .0109
found = 1/92
C = []
coinAmt = []
turns = []
class player():
    def __init__(self):
        self.coins = 0
        self.repeat = 1/92
        self.turns = {}
        for i in range(0, 93):
            self.turns[i] = 0
        self.level = {}
        self.numFound = 0
        self.lessen = .0109
        for i in range(0, 93):
            self.level[i] = random.randint(1, (i*2)+1)
    
    def play(self):
        while self.numFound < 92:
            self.turns[self.numFound]+=1
            self.coins += self.level[self.numFound]
            chance = 1-(self.repeat*self.numFound-
                        lessen*
                        (self.level[self.numFound]-1))
            if(random.random() < chance):
                self.numFound+=1
                
            if self.turns[self.numFound] > 10000:
                break
                
    def fitness():
        return self.coins
class pool():
    
    def __init__(self, n):
        self.n = n
        self.players = [player() for x in range(n)]
        self.generationNum = 0
    def evolve(self):
        for p in self.players:
            p.play()
    def selection(self):
        total = sum(p.coins for p in self.players)
        total += 10*sum(sum(p.turns.values()) for p in self.players)
        self.players.sort(key = lambda x: x.coins+10*(sum(x.turns.values())))
        select = []
        for i in self.players:
            select.append((i.coins+sum(i.turns.values())*10)/total)
            
        #select.sort(key = lambda x: x)
        select = select[::-1]
        select = list(accumulate(select))
        print("Top 10 in Generation "+str(self.generationNum)+":")
        for i in range(10):
            print(str(self.players[-i-1].coins)+" coins used in "+str(sum(self.players[-i-1].turns.values())) +" turns")
            
        select[-1] = 1
        results = []
        for i in range(self.n):
            firstChoice = next(x[0] for x in enumerate(select) if x[1] >= random.random())
            secondChoice= next(x[0] for x in enumerate(select) if x[1] >= random.random())
            results.append((firstChoice, secondChoice))
        self.breed(results)
            
    def breed(self, results):
        newPlayers = []
        self.generationNum+=1
        for i in range(self.n):
            level1 = self.players[results[i][0]].level
            level2 = self.players[results[i][1]].level
            newLevel = {}
            for k in level1:
                newLevel[k] = self.mutate(level1[k], level2[k])
            newPlayers.append(player())
            newPlayers[-1].level = newLevel
        self.players = newPlayers
            
                
    def randSign(self):
        if(random.random() < .5):
            return -1
        else:
            return 1     
    def mutate(self, v1, v2):
        avg = (v1+v2)/2
        return max(1, int(avg + random.randint(0,max(1,int(avg/2)))*self.randSign()))
    def reportBack(self):
        results = [Counter(i.level) for i in self.players]
        results = sum(results, Counter())
        for k in results:
            results[k] = results[k]/self.n
            print("For level "+str(k)+", "+str(results[k])+" number of coins is recommended")
        return results