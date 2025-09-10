VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0
    
    for card in hand:
        # if card == 'Ace':
        #     del hand.index('Ace') ## hand[0]:
        #     for card in hand:
                
        #     score += 1 or

        
        # if total point except ace >= 10  +11
        # if total point ex ace > 11, busted
        if card == 'Ace':
        # if total point except ace > 20, +1 
            'Ace' == 1
        # if total point except ace < 11  +11
            'Ace' == 11
        elif card in ['Jack', 'King', 'Queen']:
            score += 10
        else:
            score += card
    return score