import random
import itertools
from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA

RANK_ORDER = '1234567890JQKA'
SUIT_ORDER = 'DCHS'
POKER_ORDER = ['straight', 'flush', 'full house', 'four of a kind', 'straight flush']
RANK_ARRAY = list(RANK_ORDER)
SUIT_ARRAY = list(SUIT_ORDER)

def sort_cards(cards):
    sorted_hand = sorted(cards, key=Card_Key)
    return sorted_hand

def Card_Key(card):
    rank_score = RANK_ARRAY.index(card[0])
    suit_score = SUIT_ARRAY.index(card[1])
    return rank_score, suit_score

def is_pair(card1, card2):
    if RANK_ARRAY.index(card1[0]) == RANK_ARRAY.index(card2[0]):
        return True
    else:
        return False

def get_pairs(cards):
    cards = sort_cards(cards)
    pairs = []
    for i in range(len((cards)) - 1):
        if RANK_ARRAY.index(cards[i][0]) == RANK_ARRAY.index(cards[i + 1][0]):
            pairs.append([cards[i], cards[i+1]])
    return pairs

def is_three(card1, card2, card3):
    if RANK_ARRAY.index(card1[0]) == RANK_ARRAY.index(card2[0]) and RANK_ARRAY.index(card1[0]) == RANK_ARRAY.index(
            card3[0]):
        return True
    else:
        return False

def get_threes(cards):
    cards = sort_cards(cards)
    threes = []
    for i in range(len((cards)) - 2):
        if RANK_ARRAY.index(cards[i][0]) == RANK_ARRAY.index(cards[i+1][0]) and RANK_ARRAY.index(cards[i][0]) == RANK_ARRAY.index(cards[i+2][0]):
            threes.append([cards[i], cards[i+1], cards[i+2]])
    return threes    

def get_fours(cards):
    cards = sort_cards(cards)
    fours = []
    for i in range(len((cards)) - 3):
        if RANK_ARRAY.index(cards[i][0]) == RANK_ARRAY.index(cards[i+1][0]) and RANK_ARRAY.index(cards[i][0]) == RANK_ARRAY.index(cards[i+2][0]) and RANK_ARRAY.index(cards[i][0]) == RANK_ARRAY.index(cards[i+3][0]):
            fours.append([cards[i], cards[i+1], cards[i+2], cards[i+3]])
    return fours     

def is_a_full_house(cards):
    cards_list = sort_cards(cards)
    if is_pair(cards_list[0], cards_list[1]) and is_three(cards_list[2], cards_list[3], cards_list[4]):
        return True
    elif is_three(cards_list[0], cards_list[1], cards_list[2]) and is_pair(cards_list[3], cards_list[4]):
        return True
    else:
        return False

def all_full_houses(hand):
    house_list = []
    for item in itertools.combinations(hand, 5):
        # print(item)
        if is_a_full_house(item):
            house_list.append([item[0], item[1], item[2], item[3], item[4]])
    return house_list

def is_straight(play):
    cards = sort_cards(play)
    i = 0
    for x in range(len(cards) - 1):
        if RANK_ARRAY.index(cards[x + 1][0]) == RANK_ARRAY.index(cards[x][0]) + 1:
            i = i + 1
    if i == 4:
        return True
    else:
        return False

def is_flush(cards):
    i = 0
    for x in range(len(cards)):
        if SUIT_ARRAY.index(cards[0][1]) == SUIT_ARRAY.index(cards[x][1]):
            i = i + 1
    if i == 5:
        return True
    else:
        return False

def all_straights(hand):
    straights_list = []
    for item in itertools.combinations(hand, 5):
        # print(item)
        if is_straight(item):
            straights_list.append([item[0], item[1], item[2], item[3], item[4]])
    return straights_list

def all_flush(hand):
    flush_list = []
    for item in itertools.combinations(hand, 5):
        # print(item)
        if is_flush(item):
            flush_list.append([item[0], item[1], item[2], item[3], item[4]])
    return flush_list

def all_straight_flush(hand):
    straight_flush_list = []
    for item in itertools.combinations(hand, 5):
        # print(item)
        if is_straight_flush(item):
            straight_flush_list.append([item[0], item[1], item[2], item[3], item[4]])
    return straight_flush_list

def is_straight_flush(cards):
    if is_straight(cards):
        if is_flush(cards):
            return True
        else:
            return False
    else:
        return False

def get_fives(hand):
    straights = all_straights(hand)
    flushs = all_flush(hand)
    full_houses = all_full_houses(hand)
    straight_flushs = all_straight_flush(hand)
    fives = []
    for x in straights:
        fives.append(x)
    for x in flushs:
        fives.append(x)
    for x in full_houses:
        fives.append(x)
    for x in straight_flushs:
        fives.append(x)
    return fives

def best_play(cards):
    fives = get_fives(cards)
    fours = get_fours(cards)
    threes = get_threes(cards)
    pairs = get_pairs(cards)
    if fives:
        return get_play_type(fives[-1])
    elif fours:
        return get_play_type(fours[-1])
    elif threes:
        return get_play_type(threes[-1])
    elif pairs:
        return get_play_type(pairs[-1])   
    else:
        return 'high card'
    
def get_play_type(play):
    if len(play) == 1:
        return 'single'
    elif len(play) == 2:
        return 'pair'
    elif len(play) == 3:
        return 'triple'
    elif len(play) == 5:
        i = 0
        for x in range(len(play) - 1):
            if RANK_ARRAY.index(play[x + 1][0]) == RANK_ARRAY.index(play[x][0]) + 1:
                i = i + 1
        suit = play[0][1]
        x = 0
        for card in play:
            if card[1] == suit:
                x = x + 1
        if i == 4 and x == 5:
            return 'straight flush'
        elif i == 4:
            return 'straight'
        elif x == 5:
            return 'flush'
        else:
            if is_pair(play[0], play[1]) and is_three(play[2], play[3], play[4]):
                return 'full house'
            elif is_three(play[0], play[1], play[2]) and is_pair(play[3], play[4]):
                return 'full house'
            else:
                if is_four_kind(play):
                    return 'four of a kind'


def play(player, flop, current_bet, players_still_in):

    hand = player['hand'] + flop

    if current_bet > player['funds']:
        return 'fold'
    else:
        if best_play(hand) in POKER_ORDER:
            return 'raise ' + str(round(player['funds'] / 2))
        else:
            return 'raise 10'
    
# return formatting:
# for fold, return 'fold'
# for raise, return 'raise {amount}' e.g 'raise 10'
# for call, return 'call'

