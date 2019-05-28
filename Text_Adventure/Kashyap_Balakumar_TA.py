from __future__ import print_function
import random

'''We broke this game up into functions to make it easier to navigate, call, and
exit from. We were able to create functions for stuff we used repeatedly and
for the squences to make the code a lot easier to read and code.'''

#Start method calls all other methods and functions
def start():
    #Gameplay variables
        #Stats that player can choose
    attack = 0
    hearts = 0
    run = 0
    
    #Gameplay methods and functions
    intro_text()
    
    want = want_to_play()
    
    if want == False:
        return
    
    stats = choose_stats()
    attack = stats[0]
    hearts = stats[1]
    run = stats[2]
    
    stats = s1(attack, hearts, run)
    attack = stats[0]
    hearts = stats[1]
    run = stats[2]
    
    stats = s2(attack, hearts, run, 5)
    attack = stats[0]
    hearts = stats[1]
    run = stats[2]
    lastEnemy = stats[3]
    
    stats = s3(attack, hearts, run, 5, lastEnemy)
    attack = stats[0]
    hearts = stats[1]
    run = stats[2]
    lastEnemy = stats[3]
    
    stats = s4(attack, hearts, run, 5, lastEnemy)
    attack = stats[0]
    hearts = stats[1]
    run = stats[2]
    lastEnemy = stats[3]
    
    stats = s5(attack, hearts, run, 5, lastEnemy)
    attack = stats[0]
    hearts = stats[1]
    run = stats[2]
    
    s6(attack, hearts, run, 5)
    
#-------------------------------------------------------------------------------  
#Intro method to print intro text
def intro_text():
    '''Introduction text, the first text displayed when game is run'''
    print("\n\nHello, welcome to the world of")
    print("OGGIE'S ADVENTURE")

#-------------------------------------------------------------------------------
def want_to_play():
    '''Asks user wether they actually want to play this game'''
    play = raw_input("\n\nWould you like to play? y/n (y/n stands for yes/no" \
    " type y or n to contine on with the game): ")
    
    #Game has started if user chooses'y'
    if play == 'y':
        print("\nTime to chose your stats.")
        print("\nThere are three categories, attack, hearts, and runs")
        print("\nYou get 10 points to spend, you can't change the points" \
        "after you've applied them, but armour, weapons, and powerups you get"\
        " can change them.")
    elif play == 'n':
        #Stops gameplay if user chooses 'n'
        return False
    else:
        other_text()
        return False
        
    return True

#-------------------------------------------------------------------------------
def choose_stats():
    '''This is used to create a part of the game for the user to pick their
    stats, attack power, hearts, and more, which will be essential to their
    success in the game'''
    attack = int(raw_input("\n\nNow time to pick your attack stat(input number"\
    " equal to how many stat points you have left): "))
    hearts = 0
    run = 0
    
    broken = True
    
    if attack != int(attack) or attack > 10:
        broken = other_text()
        return
    
    #Conditionals are used to make sure user doesn't overload on stats
    if 10-attack > 0:
        hearts = int(raw_input("\nChose how many hearts you want to have."\
        " You have " + str(10-attack) + " points left: "))
        if hearts != int(hearts) or hearts > 10-attack:
            broken = other_text()
            return
        
    if broken == False:
        return
        
    if 10-attack-hearts > 0:
        run = int(raw_input("\nIn this game you have a set amount of times you" \
        " can run away from battle, the only way to ensure 100% survival and this" \
        " is also tied with your stat points. You have " + str(10-attack-hearts) +
        " points left: "))
        if run != int(run) or run > 10-attack-hearts:
            broken = other_text()
            return
    
    if broken == False:
        return
            
    return [attack, hearts, run]

#---------------------------------S1--------------------------------------------
#First sequence of gameplay
def s1(currA, currH, currR):
    '''We broke the sqeunces of the game into functions to make them easier to 
    navigate and read, as well as exit from, this is the first of those
    sqeunces. Also the sqeunces are very similar in layout so after one, we
    could just use that as a template. The first squences is about you waking
    up or not which can lead to two different senarios.'''
    #Reset stats to make Oggie more powerful
    attack = currA
    hearts = currH
    run = currR
    
    #Initial user input
    action = raw_input("\n\nWould you like to wake up?(If you go back to sleep" \
    " there is a high possiblity that you could die) y/n: ");
    
    #Boolean used to return from the function if user loses to prevent further gameplay
    not_again = True
    
    if action == 'y':
        print("\nYou have woken up from a long slumber and are very hungry!!")
    elif action == 'n':
        print("\nYou go back to sleep for five months.")
        
        if random.randint(1, 5) == 1:
            print("\nYou wake up and feel stronger. you get ten more stat points")
            
            #Player chooses stats that affects later gameplay
            attack = int(raw_input("\nYou now have 20 points to spend, now pick" \
            " your new attack stat: "))
            
            if 20-attack > 0:
                hearts = int(raw_input("\nChose how many hearts you want to have. You have "
                + str(20-attack) + " points left: "))
                
            if 20-attack-hearts > 0:
                run = int(raw_input("\nIn this game you have a set amount of times" \
                " you can run away from battle, the only way to ensure 100% survival" \
                " and this is also tied with your stat points. You have "
                + str(20-attack-hearts) + " points left: "))
                
        else:
            print("\nYou wake up and go outside. You see meteors falling from the" \
            " sky. One crashes in front of you and...")
            print("\nGAME OVER!!")
            
            action = raw_input("\nWould you like to play again? y/n: ")
            
            if action == 'y':
                start()
            elif action == 'n':
                not_again = False
    else:
        other_text()
        return
        
    if not_again == False:
        return
    
    return [attack, hearts, run]
    
#--------------------------------Fight Sequence---------------------------------
#Fight sequence
def fight_sequence(attack, hearts, total, enemy):
    '''This subtracts one of your hearts for the damage your foes do and them 
    using your attak damage subtracts from the enemy's health(total). This will
    test your stat choices later on'''
    original = hearts
    if total > 0:
        hearts = hearts - 1
        total = total - attack
        if total > 0:
            hearts = fight_sequence(attack, hearts, total, enemy)
    
    return hearts
    
#------------------------------------S2-----------------------------------------    
#Second sequence of gameplay
def s2(attack, hearts, run, total):
    '''In the second squence we use if statements to create different paths of 
    which you can choose to follow and fight from. This would include fairies or
    bandits'''
    print("\n\nBecause of your hunger you go out to explore and find food.")
    
    action = raw_input("\nWould like to go into the forest? y/n: ")
    enemy = ''
    
    if action == 'y':
        enemy = 'FAIRIES'
        print("\nYou go into the forest and walk past some trees.")
        print("\nAs you pass the tree you feel a pain near you back.")
        print("\nYou turn to see a group of FAIRIES with swords ready to fight.")
    elif action == 'n':
        enemy = 'BANDITS'
        print("\nYou don't go into the forest and go on the road instead.")
        print("\nYou hear a rustling from the bush near you.")
        print("\nA gang of BANDITS appear ready to fight you and take your stuff")
    
    fight = raw_input('\n\nWould you like to fight? y/n: ')
    
    original = hearts
    
    if fight == 'y':
        hearts = fight_sequence(attack, hearts, total, enemy)
    elif fight == 'n':
        if run > 0:
            print("\nYou run away out of fear.")
            print("\nYou lost 1 run point.")
            run = run - 1
        else:
            print("\nYou cannot run.")
            print("\nYou have no run points!!")
            print("\nYou must fight.")
            
            hearts = fight_sequence(attack, hearts, total, enemy)
    else:
        other_text()
        return
    
    print("\nYou defeated the " + enemy + "!")
    print("\nBut you did lose " + str(original-hearts) + " health points ):")
    
    return [attack, hearts, run, enemy]

#-----------------------------------S3------------------------------------------
#Third sequence of gameplay
def s3(attack, hearts, run, total, enemy):
    '''Sequence 3 to 5 are very similar in the manner that you go into a dungeon
    and choose to fight enemies, which we used an if statement to change the 
    outcome of based on the input. Sequence 3 contains orcs'''
    action = raw_input("\n\nWould like to go into the dungeon? y/n: ")
    enemy = ''
    
    if action == 'y':
        enemy = 'ORCS'
        print("\nYou go into the dark deugon and walk past some cells.")
        print("\nYou turn a corner and see an ORC.")
        print("\nYou take a better look and it is a group of "\
        "ORCS with giant clubs.")
    elif action == 'n':
        return [attack, hearts, run, enemy]
    
    fight = raw_input('\n\nWould you like to fight? y/n: ')
    
    original = hearts
    
    if fight == 'y':
        hearts = fight_sequence(attack, hearts, total, enemy)
    elif fight == 'n':
        if run > 0:
            print("\nYou run away out of fear.")
            print("\nYou lost 1 run point.")
            run = run - 1
        else:
            print("\nYou cannot run.")
            print("\nYou have no run points!!")
            print("\nYou must fight.")
            
            hearts = fight_sequence(attack, hearts, total, enemy)
    else:
        other_text()
        return
    
    print("\nYou defeated the " + enemy + "!")
    print("\nBut you did lose " + str(original-hearts) + " health points ):")
    
    return [attack, hearts, run, enemy]
    
#---------------------------------S4--------------------------------------------
#Fourth sequence of gameplay
def s4(attack, hearts, run, total, enemy):
    '''Sequence 3 to 5 are very similar in the manner that you go into a dungeon
    and choose to fight enemies, which we used an if statement to change the 
    outcome of based on the input. Sequence 4 contains prisoners'''
    enemy = 'PRISONERS'
        
    print("\n\nYou turn another few corners.")
    print("\nYou out of the corner of your eye you see some PRISONERS.")
    print("\nThey seem to have gotten free.")
  
    
    fight = raw_input('\n\nWould you like to fight? y/n: ')
    
    original = hearts
    
    if fight == 'y':
        hearts = fight_sequence(attack, hearts, total, enemy)
        print('\n\nAfter the fight you found some food on the prisoners.'\
        ' You have regained some hearts.')
        hearts = hearts + 2
    elif fight == 'n':
        if run > 0:
            print("\nYou run away out of fear.")
            print("\nYou lost 1 run point.")
            run = run - 1
        else:
            print("\nYou cannot run.")
            print("\nYou have no run points!!")
            print("\nYou must fight.")
                
            hearts = fight_sequence(attack, hearts, total, enemy)
    else:
        other_text()
        return
        
    print("\nYou defeated the " + enemy + "!")
    print("\nBut you did lose " + str(original-hearts) + " health points ):")
    
    return [attack, hearts, run, enemy]

#--------------------------------S5---------------------------------------------
#Fifth sequence of gameplay 
def s5(attack, hearts, run, total, enemy):
    '''Sequence 3 to 5 are very similar in the manner that you go into a dungeon
    and choose to fight enemies, which we used an if statement to change the 
    outcome of based on the input. Sequence 4 contains skeletons'''
    enemy = 'SKELETON'
        
    print("\n\nYou see a light, it is the exit.")
    print("\nYou are about to leave but come face to face with a gang of "\
    "SKELETONS")
  
    
    fight = raw_input('\n\nWould you like to fight? y/n: ')
    
    original = hearts
    
    if fight == 'y':
        hearts = fight_sequence(attack, hearts, total, enemy)
        print('\n\nAfter the fight you found a glowing sword and some armour.'\
        ' You are deciding wether to take it or not ...'\
        "(Looks like the character took the sword and armour while I was "\
        "explaining this.) Anyways your attack and health went up.")
    elif fight == 'n':
        if run > 0:
            print("\nYou run away out of fear.")
            print("\nYou lost 1 run point.")
            run = run - 1
        else:
            print("\nYou cannot run.")
            print("\nYou have no run points!!")
            print("\nYou must fight.")
            
            hearts = fight_sequence(attack, hearts, total, enemy)
    else:
        other_text()
        return
    
    print("\nYou defeated the " + enemy + "!")
    print("\nBut you did lose " + str(original-hearts) + " health points ):")
    
    return [attack, hearts, run]

#--------------------------------Final S6---------------------------------------
#Final boss sequence
def s6(attack, hearts, run, total):
    '''This is the final boss fight everyone has been waiting for, though it may
    seem like any other fight sequence in the game, this will challenge your
    choices of stats and how many times you fought or ran. We use the fight
    sequence functions and change the stats of enemies to make the fights harder
    or easier'''
    enemy = 'FINAL BOSS'
        
    print("\n\nYou leave the duegon behond and move forward, as you look behind"\
    " you ram into the wall of a castle that was not there before.")
    print("\nYou enter and there seems to nothing inside, except darkness that"\
    " seems to move with you. ")
    print("\nYou enter a large room with tables and goblets. You see moutains"\
    " of gold at the end of the room.")
    print("\nYou take a step forward and the darkness begins to form an entity"\
    " in between you and the gold.")
    print("The doors behind you shut closed and the room is envolved in a black"\
    " light. You know this not a fight you can run from.")
  
    
    fight = raw_input('\n\nWould you like to fight? y/n: ')
    
    if fight == 'y':
        hearts = fight_sequence(attack, hearts, total, enemy)
        print("\nYou have defeated the " + enemy + "!!")
        print("\nYou have beaten the game!")
        print("\nThank you hero for saving this land!!!!")
        print("\n\nThe End")
        restart()
        
    elif fight == 'n':
        print("\nYou cannot run.")
        print("\nYou must fight.")
            
        hearts = fight_sequence(attack, hearts, total, enemy)
    else:
        other_text()
        return

#-------------------------------------------------------------------------------
#Other text method
def other_text():
    print("\n\nGAME OVER!!")
    print("\nYou typed in text you weren't supposed to")
    output = restart()
    return output

#-------------------------------------------------------------------------------
#Restart method
def restart():
    action = raw_input("\nWould you like to play again? y/n: ")
            
    if action == 'y':
        start()
    else:
        return False
    
    return True
    
    
#Starting gameplay
start()
    