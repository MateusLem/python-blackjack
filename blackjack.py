from random import randint

def create_cards():
    return {
    1:'A',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9',
    10:'10',
    11:'J',
    12:'Q',
    13:'K'
}

def create_deck():
    cards = create_cards()
    return [{key: value} for _ in range(4) for key, value in cards.items()]

def create_hand(deck: list):
    hand = []
    for _ in range(2):
        reach = len(deck) - 1
        id = randint(0, reach)

        hand.append(deck[id])
        deck.pop(id)

    hand = dict_to_hand(hand)
    return hand, deck

def dict_to_hand(hand:list):
    return [value for id, item in enumerate(hand) for key, value in item.items()]

def points(hand:list):
    points=0
    for card in hand:
        match card:
            case 'K' | 'Q' | 'J':
                points += 10
            case 'A' if hand[0] in 'KQJ' or hand[1] in 'KQJ':
                points += 11
            case 'A':
                points += 1
            case _:
                points += int(card)

    return points

def result(hand=list):
    points = points(hand)

    if points == 21:
        return 'Won'

    if points>21:
        return 'Lost'
    
def show_result():
    turn = result(hand_user)
    if turn:
        print(result)
        return True
    
def hit(deck: list, hand:list):
    '''
    Add a card to a hand
    '''
    card = []
    reach = len(deck) - 1
    id = randint(0, reach)
    card.append(deck[id])
    deck.pop(id)

    card = dict_to_hand(card)
    hand.extend(card)

    return hand, deck
