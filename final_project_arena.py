# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 08:15:17 2023

@author: brian.kelly
"""

import tbc




def main():
       hero = tbc.Character()
       print("Hello, and welcome to the arena simulator, where we pit various")
       print("warriors against eachother to see who is the strongest")
       print("The current classes availble are: Fighter, Tank, Marksman, Bruiser, Weakling, and Demon")
       character = input("Select the class of the first fighter")
        
       if character.startswith("Fighter"):
           hero.name = "Figther"
           hero.hitPoints = 20
           hero.hitChance = 50
           hero.maxDamage = 5
           hero.armor = 2
    
       elif character.startswith("Tank"):
            hero.name = "Tank"
            hero.hitPoints = 30
            hero.hitChance = 30
            hero.maxDamage = 7
            hero.armor = 3
        
       elif character.startswith("Marksman"):
            hero.name = "Marksman"
            hero.hitPoints = 15
            hero.hitChance = 70
            hero.maxDamage = 4
            hero.armor = 1
            
       elif character.startswith("Bruiser"):
            hero.name = "Bruiser"
            hero.hitPoints = 25
            hero.hitChance = 20
            hero.maxDamage = 10
            hero.armor = 0
            
       elif character.startswith("Weakling"):
            hero.name = "Weakling"
            hero.hitPoints = 10
            hero.hitChance = 50
            hero.maxDamage = 1
            hero.armor = 0
            
       elif character.startswith("Demon"):
            hero.name = "Demon"
            hero.hitPoints = 50
            hero.hitChance = 100
            hero.maxDamage = 50
            hero.armor = 3
        
       else:
            print("Invalid response")
    
       oppenent = input("Now, give me the class of the opponent")
        
       if oppenent.startswith("Fighter"):
    
            monster = tbc.Character("Fighter", 20, 50, 5, 2)
        
       elif oppenent.startswith("Tank"):
    
            monster = tbc.Character("Tank", 30, 30, 7, 5)
        
       elif oppenent.startswith("Markman"):
    
            monster = tbc.Character("Markman", 15, 70, 4, 1)
        
       elif oppenent.startswith("Bruiser"):
    
            monster = tbc.Character("Bruiser", 25, 20, 10, 0)
        
       elif oppenent.startswith("Weakling"):
    
            monster = tbc.Character("Weakling", 10, 50, 1, 0)
        
       elif oppenent.startswith("Demon"):
    
           monster = tbc.Character("Demon", 50, 100, 50, 3)
        
       else:
            print ("Invalid response")
        
       print("Alright then! LET'S GET READY TO RUUUUUUUUMBLEEEEEEEE!!!!!!")
    
       hero.printStats()
       monster.printStats()
       tbc.fight(hero, monster)
            
    
    
    
if __name__ == "__main__":
    main()
