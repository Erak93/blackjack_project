import random
import os

import emoji

from art import logo



def deal_cards():
    """Returns a random card from the deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculate from the cards"""
    if sum(cards)==21 and len(cards)==2: # a hand with only 2 cards ace+10 is a blackjack(0)
        return 0
    if 11 in cards and sum(cards)>21: # if the score is already above 21 but there is an ace(usually 11), the ace becomes 1
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score,computer_score):
    if user_score==computer_score:
        return f'It is a Draw {emoji.emojize(":grinning_face_with_big_eyes:")}'
    elif computer_score==0:
        return f'You lose {emoji.emojize(":winking_face_with_tongue:")}, your opponent has Blackjack'
    elif user_score==0:
        return f'You win {emoji.emojize(":winking_face_with_tongue:")}, you have a Blackjack'
    elif user_score>21:
        return f'You went over {emoji.emojize(":winking_face_with_tongue:")}'
    elif computer_score>21:
        return f'You won {emoji.emojize(":winking_face_with_tongue:")}, opponent went over'
    elif user_score>computer_score:
        return f'You won {emoji.emojize(":winking_face_with_tongue:")}, nobody has a blackjack, you are below 21 and have a higher score'
    else:
        return "You lose"




def play_game():
    print(logo)
    user_cards=[]
    computer_cards=[]
    is_game_over=False

    for _ in range(2):
        
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:

        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another cards, type 'n' to pass: ")
            if user_should_deal=='y':
                user_cards.append(deal_cards())
            else:
                is_game_over=True



    while computer_score!=0 and computer_score<17: # the computer keeps drawing cards as long as the score is below 17
        computer_cards.append(deal_cards())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand {user_cards},final score is {user_score}")
    print(f"The computer final hand is {computer_cards}, their final score is {computer_score}")

    print(compare(user_score,computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=="y":
    
    clear=lambda: os.system('clear')
    clear()
    play_game()