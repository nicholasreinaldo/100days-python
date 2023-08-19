rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choices = [rock, paper, scissors]
random_num = random.randint(0,2)
random_choice = choices[random_num]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice < 0 or player_choice >= 3:
    print("Invalid choice, please try again.")
else:
    player_choose = print(choices[player_choice])
    computer_choose = print("Computer chose:\n" + random_choice)
    if player_choice == 0 and random_num == 2:
        print("You won.")
    elif player_choice == 1 and random_num == 0:
        print("You won.")
    elif player_choice == 2 and random_num == 1:
        print("You won.")
    elif player_choice == 0 and random_num == 1:
        print("You lose.")
    elif player_choice == 1 and random_num == 2:
        print("You lose.")
    elif player_choice == 2 and random_num == 0:
        print("You lose.")
    elif player_choice == random_num:
        print("It's a draw.")