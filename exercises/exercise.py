import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_card = []
computer_card = []
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

for starting_card in range(2):
    player_card.append(random.choice(cards))
    computer_card.append(random.choice(cards))

print(computer_card[1])
print(computer_card)
