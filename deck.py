from random import shuffle

num_land = 24
num_creatures = 20
num_spells = 16

cards = []

for i in range(num_land):
    cards.append('land')

for i in range(num_creatures):
    cards.append('creature')

for i in range(num_spells):
    cards.append('spells')

shuffle(cards)
shuffle(cards)
shuffle(cards)

#for card in cards:
#    print(card)

num_players = 3
num_initial_number_of_cards = 7
for player in range(num_players):
    player_cards = []
    for card in range(num_initial_number_of_cards):
        player_cards.append(cards.pop())
    for card in player_cards:
        print(card)
    print('')


