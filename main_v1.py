from art import logo
import random
import emoji
game_over=False

blackjack_cards=[1,2,3,4,5,6,7,8,9,10]
goal=21
player_hand=[]
dealer_hand=[]
player_score=sum(player_hand)
dealer_score=sum(dealer_hand)

def deal_cards(number_of_cards):
    for i in range(number_of_cards):
        player_hand.append(random.choice(blackjack_cards))
        dealer_hand.append(random.choice(blackjack_cards))

def calc_points():
    player_score=sum(player_hand)
    dealer_score=sum(dealer_hand)
    if player_score==goal:
        print(f'Your score is {player_score}. The dealer hand is {dealer_score}.You won {emoji.emojize(":grinning_face_with_big_eyes:")}')
        return "GAME OVER"
    elif player_score>goal:        
        print( f'Your score is {player_score}. You lost {emoji.emojize(":winking_face_with_tongue:")}')
        return"GAME OVER"
    elif dealer_score>goal and player_score<=goal:
        print( f'Your score is {player_score}. The dealer hand is {dealer_score}.You won {emoji.emojize(":grinning_face_with_big_eyes:")}')
        return "GAME OVER"
    elif player_score <goal and dealer_score<goal:
        return f"Your hand is {player_score}. The first card of the dealer's hand is {dealer_hand[0]}."


while game_over==False:
    start_game=input("Do you want to play blackjack? Y/N: ").upper()
    turns_counter=1
    if start_game=="Y":
        print(logo)
        if turns_counter==1:
            deal_cards(3)
            turns_counter+=1

        elif turns_counter>1:
            deal_cards(1)

        print(player_hand)
        print(dealer_hand)
        calc_points()
        
   
    
        if calc_points()=="GAME OVER":
            game_over=True
        else:
            print(calc_points())

      
    else:
        game_over=True
    
    

