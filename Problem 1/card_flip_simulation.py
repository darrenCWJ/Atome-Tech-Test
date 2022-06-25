import random
import numpy as np

def flip_cards_simulation(x):
    deck_cards = [0] * 54
    for i in x:
        # flip the top card
        print(f'flipping {i} cards')
        print(deck_cards)
        for j in range(i):
            if deck_cards[j] == 1:
                deck_cards[j] = 0
            else:
                deck_cards[j] = 1
        print(deck_cards)
        # once flip shuffle the cards
        random.shuffle(deck_cards)
    return deck_cards

if __name__ == '__main__':
    lis = []
    simul = 100000
    x = [30,27,28,33,1,25]
    for i in range(simul):
        deck_of_cards = flip_cards_simulation(x)
        print(np.mean(deck_of_cards))
        lis.append(np.mean(deck_of_cards))
    
    average = np.mean(lis)
    print(f'bootstrap expected: {average}')