# -*- coding: utf-8 -*-
"""
Created on Sat Dec 05 12:49:33 2015

@author: Blake
"""
print("Start Game")
print("Press enter to continue")
#pause = raw_input()

hero_hp = 200
hero_ap = 50
bf_ap = 30
bf_hp=100

import random 

while (hero_hp > 0) & (bf_hp > 0) :     #loop continues while both opponents' health is > 0
    dieroll = random.randrange(1,6)
    damage = dieroll + hero_ap
    bf_hp = bf_hp - damage
    dieroll = str(dieroll)    
    damage = str(damage)
    bf_health = str(bf_hp)
    print("You rolled a " +dieroll)
    print("You dealt BileFoot " +damage+ " damage.  He has " +bf_health+
    " hitpoints left")
    if bf_hp <=0:
        print("You have defeated BileFoot!")
        break
    
    print("Press Enter to Continue.")
    pause = raw_input()
    
    dieroll = random.randrange(1,6)
    damage = dieroll + bf_ap
    hero_hp = hero_hp - damage
    dieroll = str(dieroll)    
    damage = str(damage)
    hero_health = str(bf_hp)
    print("BileFoot rolled a " +dieroll)
    print("BileFoot dealt you " +damage+ " damage.  You have " +hero_health+
    " hitpoints left")
    if hero_hp <=0:
        print("BileFoot has defeated you!")
        break    
    print("Press Enter to Continue.")
    pause = raw_input()
    
print("Game over")
