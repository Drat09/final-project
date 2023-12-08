# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 08:37:34 2023

@author: brian.kelly and Dominick Smith
"""

import random

class Character(object):
    
    def __init__(self, name = "Unknown", hitPoints = 0, hitChance = 0, maxDamage = 0, armor = 0):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        if type(value) == int:
            if value >= 0:
                self.__hitPoints = value
            else:
                print("input must be positive")
                self.__hitPoints = 1
        else:
            print("input must be positive")
            self.__hitPoints = 1
    
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        if type(value) == int:
            if value >= 0:
                self.__hitChance = value
            else:
                print("input must be positive")
                self.__hitChance = 1
        else:
            print("input must be positive")
            self.__hitChance = 1
    
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        if type(value) == int:
            if value >= 0:
                self.__maxDamage = value
            else:
                print("input must be positive")
                self.__maxDamage = 1
        else:
            print("input must be positive")
            self.__maxDamage = 1
    
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        if type(value) == int:
            if value >= 0:
                self.__armor = value
            else:
                print("input must be positive")
                self.__armor = 1
        else:
            print("input must be positive")
            self.__armor = 1
    
    
    
    def printStats(self):
        print(f"""
 Name = {self.__name}""")
        print(f"HP = {self.__hitPoints}")
        print(f"HC = {self.__hitChance}")
        print(f"MD = {self.__maxDamage}")
        print(f"A = {self.__armor}")
    
def main():
    good = Character()
    good.name = "Good"
    good.hitPoints = 15
    good.hitChance = 70
    good.maxDamage = 5
    good.armor = 1
    
    good.printStats()
    
    evil = Character()
    evil.name = "Evil"
    evil.hitPoints = 20
    evil.hitChance = 40
    evil.maxDamage = 7
    evil.armor = 2
    
    
    evil.printStats()
    
    fight(good,evil)
    
def fight(player1, player2):
    player1HP = player1.hitPoints
    player1HC = player1.hitChance
    player1MD = player1.maxDamage
    player1A = player1.armor
    
    player2HP = player2.hitPoints
    player2HC = player2.hitChance
    player2MD = player2.maxDamage
    player2A = player2.armor
    
    keepGoing = True
    while keepGoing:
        if player1HP <= 0 and player2HP <= 0:
            print ("It's a draw!")
            keepGoing = False
        else:
            if player1HP > 0:
                if player2HP > 0:
                    input("""
Press ENTER for next round
                          """)
                    hitTest1 = random.randint(0,100)
                    if player1HC >= hitTest1:
                        print(f"""
{player1.name} hits {player2.name}...
""")
                        damage1 = random.randint(1, player1MD)
                        print(f" for {damage1} points of damage")
                        print(f" {player2.name}'s armor can absorb {player2.armor} pints of damage")
                        if damage1 >= player2A:
                            damage1 = damage1 - player2A
                        else:
                            damage1 = 0
                        if damage1 > player2HP:
                            player2HP = damage1 - player2HP
                        else:
                            player2HP = player2HP - damage1
                    
                        print(f"{player1.name}: {player1HP} HP")
                        print(f"{player2.name}: {player2HP} HP")
                    else:
                         print(f"""
{player1.name} missed
""")
                    hitTest2 = random.randint(0,100)
                    if player2HC >= hitTest2:
                        print(f"""
{player2.name} hits {player1.name}...
                          """)
                        damage2 = random.randint(1,player2MD)
                        print(f" for {damage2} points of damage")
                        print(f" {player1.name}'s armor can absorb {player1.armor} points of damage")
                        if damage2 >= player1A:
                          damage2 = damage2 - player1A
                        else:
                          damage2 = 0
                        if damage2 > player1HP:
                          player1HP = damage2 - player1HP
                        else:
                          player1HP = player1HP - damage2
                    
                        print(f"{player1.name}: {player1HP} HP")
                        print(f"{player2.name}: {player2HP} HP")
                    else:
                        print(f"""
{player2.name} missed
""")
                
                else:
                    print(f"""
{player1.name} wins!
""")
                    keepGoing = False
            
            else:
                print(f"""
{player2.name} wins!  
                    """)
                keepGoing = False

if __name__ == "__main__":
    main()