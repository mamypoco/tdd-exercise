VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0

    # check cards total except Ace
    if len(hand) in range(2, 6):
        for card in hand:       
            # 'Ace', skip
            if card == 'Ace':
                continue
            # if face cards
            if card in ['Jack', 'King', 'Queen']:
                score += 10
            else:
                score += card

    # check 'Ace'
    if 'Ace' in hand:
        # if total <= 20, treat Ace 1 
        if score in range (11, 21):
            score += 1
        # if score <= 11,  treat Ace 11
        elif score < 11:
            score += 11
        else:
            print("You are out!")
    print(score)
    return score

#this fucntion does not score over 21, if so print("you are out")

hand = [2, 'Queen', 'Jack', 'Ace']
print(blackjack_score(hand))

