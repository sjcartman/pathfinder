import numpy as np 
import pandas as pd
import creature
import dice
creatures = []
players = []

def set_players():
    global creatures,players
    creatures = []
    for i in players:
        print(i.name)
        print("initave :")
        x
        creatures.append(i)

def battle_1():
    global creatures
    maggot = [7,False,"maggot",9,9,0,5,-1,-3,200]
    creatures.append(creature(maggot)) 

def battle_2():
    global creatures
    rat = [5,False,"rat",14,11,1,3,5,1,200]
    roach = [8,False,"CockRoach",14,12,1,6,1,0,200]
    creatures.append(creature(rat))
    creatures.append(creature(roach))

def battle_3():
    global creatures
    man1 =[4,False,"man",10,10,0,2,0,0,100]
    dog = [6,False,"dog",13,12,2,4,3,1,135]
    creatures.append(creature(man1))
    creatures.append(creature(dog))

def battle_4():
    global creatures
    farmer = [10,False,10,10,0,0,0,3,100]
    creatures.append(farmer)
    creatures.append(farmer)
    creatures.append(farmer)
def battle_5():
    global creatures
    Acolyte = [5,False,14,1,0,-1,1,3,135]
    creatures.append(Acolyte)
    creatures.append(Acolyte)   
  
def battle_6():
    global creatures
    cultist = [14,False,15,12,2,3,5,4]
    creatures.append(cultist)
def order():
    d = dice()
    global creatures
    set_players()
    battle_1()
    x = []
    for i in creature:
         max = 0
         var = None
         for j in range(0,len(creatures)):
             if max < creatures[j].order:
                max = creatures[j].order  
                var = j
    x.append(creatures.pop(var))

def battle(creatures):
    d = dice()
    fighting = True
    while fighting:
        for i in creatures:
            print(i)
            print("Attack = a")
            print("Heal = h")
            print("done = d")
            print("skip = s")
            s = input()
            if s == 'a':
                target = 0
                while(target > 0):
                    print("Selct Target")
                    for j in range(0,len(creatures)):
                        print(str(j) +" : "+creatures[j].name)
                    target = int(input())
                    print("attack roll")
                    attack_roll = 0
                    if creatures[j].player:
                        attack_roll = d.d20() + creatures[j].to_hit
                    else :
                        attack_roll = int(input)
                    if creatures[target].ac+10 <= attack_roll:
                        print("crit")
                    if creatures[target].ac <= attack_roll:
                        print('how much damage :')
                        damage = int(input())
                        creatures[target].hp -= damage
                    else:
                        print("miss")

            elif s == 'h':
                 target = 0
                 while(target > 0):
                    print("Selct Target")
                    for j in range(0,len(creatures)):
                        print(str(j) +" : "+creatures[j].name)
                    target = int(input())
                    print('how much damage :')
                    damage = int(input())
                    creatures[target].hp += damage
            elif s == 'd':
                fighting = False
            