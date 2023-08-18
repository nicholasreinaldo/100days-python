print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_question = input('When do you plan to go explore the treasure island?\nType "day" if you want to explore right now, or type "night" if you want to explore at night.\n').lower()

if first_question == "night":
    print("Night has come and the island to dark to explore. You decided to give up.\nGame Over.")
else:
    second_question = input('You explore the island and found a suspicious looking treasure chest.\nDo you want to open it? Type "yes" to open it, or type "no" to proceed.\n').lower()
    if second_question == "yes":
        print("It turns out that the chest is a trap, it explodes as you open it and you died.\nGame Over.")
    else:
        third_question = input('You leave the chest, found the treasure and encounter a pirate.\nHe challenged you to a rock-paper-scissor game to decide who will take the treasure.\nType "rock" to use rock, type "paper" to use paper, type "scissor" to use scissor.\n').lower()
        if third_question == "scissor":
            print("You use scissor, the pirate use rock and you lost.\nThe pirate takes the treasure and leave.\nGame Over.")
        elif third_question == "rock":
            print("You use rock, the pirate use rock as well and the game is tie.\nThe pirate tricks you, run to take the treasure and leave.\nGame Over.")
        elif third_question == "paper":
            print("You use paper, the pirate use rock and you won the game.\nYou got to take the treasure. Congratulations, You Win!\n")
        else:
            print("You didn't use anything, the pirate escapes and stole the treasure. Game Over.")