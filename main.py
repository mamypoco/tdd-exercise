VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0
    
    for card in hand:       
        # if total point ex ace > 11, busted
        if card == 'Ace':
        #remove Ace from the list
            hand_wo_ace = hand.pop(hand.index('Ace')) :
        # if total point except ace > 20, treat as 1 
            if sum(hand_wo_ace) > 20:
                'Ace' == 1
        # if total point except ace < 11  treat as 11
            elif sum(hand_wo_ace) < 11:
                'Ace' == 11
        elif card in ['Jack', 'King', 'Queen']:
            score += 10
        else:
            score += card
    return score