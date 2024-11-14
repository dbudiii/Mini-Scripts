
# Online Python - IDE, Editor, Compiler, Interpreter

import random

suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
deck = [(value, suit) for suit in suits for value in values]
random.shuffle(deck)

def deal_card(deck):
    return deck.pop()

def calculate_hand_value(hand):
    for card in hand:
        value, suit = card
        
        if value in ['Jack', 'Queen', 'King']:
            total_value += 10
        elif value == 'Ace':
            total_value += 11
            ace_high_count += 1
        else:
            total_value =+ int(value)
            
        while total_value > 21 and ace_high_count > 0:
            total_value -=10 
            ace_high_count -= 1
    
    return total_value
