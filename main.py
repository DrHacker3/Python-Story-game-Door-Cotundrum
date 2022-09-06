# imports
from game import Game
from time import sleep

# Welcome
print("Hello, welcome to the game of Door cotundrum.")
sleep(1)
print("This is a simple game that you can play by yourself.")
sleep(1)

# Asking if the user wants to play
print("Shall we play the game?")

# getting user input
YesNo = input("Yes/No: ").lower()

# Yes
if YesNo == "yes":
    print("Great! Let's begin!")
    sleep(1)
    Game.start()
    
    # Getting first question 
    crossroad = input("left or right: ").lower()
    
    # Left
    if crossroad == "left":
        print("You go left and find a cave.")
        Game.cave()
        hole = input("1. use the sword to save yourself 2. keep falling down ")
        
        # Saved with sword
        if hole == "1":
            print("You use the sword to save yourself.")
            Game.caveup()
            Game.door()
            sleep(1)
            Game.end()
        
        # Keep falling down
        if hole == "2":
            print("You keep falling down.")
            Game.cavedown()
            sleep(1)
            Game.end()
            
    # Right    
    if crossroad == "right":
        print("You go right and find a river.")
        Game.river()
        river = input("1. Go through the door 2. stay and explore the river ")
        
        # Go through door
        if river == "1":
            Game.door()
            sleep(1)
            Game.end()
        
        # Explore river
        if river == "2":
            print("You stay and explore the river.")
            Game.riverexplore()
            forest_door = input("1. Go through the door 2. stay in the forest ")
            
            # Go through door
            if forest_door == "1":
                Game.door()
                sleep(1)
                Game.end()
            
            # Explore forest
            if forest_door == "2":
                print("You stay in the forest.")
                print("You find a house.")
                Game.forestHouse()
                sleep(2)
                
                # Line break for new paragraph effect
                print("")
                sleep(1)
                print("You wake up and find yourself in a hospital.")
                Game.Hospital()
                sleep(2)
                
                # Player wins the game
                Game.Win()
        

# If the user said they do not want to play
if YesNo == "no":
    print("Ok, bye!")
    exit()
