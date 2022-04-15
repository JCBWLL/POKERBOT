import itertools

cards = ['AD','JS','4D','5C','KH']
def get_suits(cards): 
        suits = []
        for i in cards:
                suits.append(i[1])
        return suits

def numeric_ranks(cards):
        suits = get_suits(cards)
        face_numbers = {'A': 14, 'J': 11, 'Q': 12, 'K': 13}
        for index, card in enumerate(cards):
                rank = card[0:-1]
                try: 
                        int(rank)
                except:
                        # Rank is a letter, not a number convert
                        cards[index] = str(face_numbers[rank])+suits[index]
        return cards

#print(numeric_ranks(cards))

def get_ranks(cards):
        """
        Returns a list of ints containing the rank of each card in cards.
        ex. 
        get_ranks(['2S','3C','5C','4D','6D'])
        returns [2,3,5,4,6]
        """
        cards = numeric_ranks(cards) # Convert rank letters to numbers (e.g. J to 11)
        rank = []
        for i in cards:
                if len(i) == 3:
                        rank.append(i[:2])
                else:
                        rank.append(i[0])     
        return rank
#print(get_ranks(cards))

def get_suits(cards):
        # returns only the suit
        return [card[-1] for card in cards]
print(get_suits(cards))

def isconcecutive(rank):
        rank = get_ranks(cards)
        a = 0
        confirm = False
        try:
                for i in rank:
                        if i == rank[a] and i == rank[a+1] and i == rank[a+2] and i == rank[a+3] and i == rank[a + 4]:
                                confirm = True
        except:
                return confirm
        return confirm
def flush(cards):
        confirm = False
        suits = get_suits(cards)
        spade = suits.count("S")
        dimond = suits.count("D")
        heart = suits.count("H")
        club = suits.count("C")
        if spade >= 5 or dimond >= 5 or heart >= 5 or club >= 5:
                confirm = True
        return confirm
'''
def evaluate_hand(hand):
        """
        Returns a string containing the name of the hand in poker.
        Input hand must be a list of 5 strings.
        ex. 
        evaluate_hand(['2S','3C','5C','4D','6D'])
        returns 'Straight'
        """
        hand = numeric_ranks(hand)
        ranks = get_ranks(hand)
        suits = get_suits(hand)
        
        if isconsecutive(rank):
        # The hand is a type of straight
        if all_equal(suits):
                # Hand is a flush
                if max(ranks) == 14:
                # Highest card is an ace
                return 'Royal flush'
                return 'Straight flush'
        return 'Straight'
        if all_equal(suits):
        return 'Flush'
        total = sum([ranks.count(x) for x in ranks])
        hand_names = {
        17: 'Four of a kind',
        13: 'Full house',
        11: 'Three of a kind',
        9: 'Two pair',
        7: 'One pair',
        5: 'High card'
        }
        return hand_names[total]


def play(player, flop, current_bet, players_still_in):

        return 'fold'
#no
# return formatting:
# for fold, return 'fold'
# for raise, return 'raise {amount}' e.g 'raise 10'
# for call, return 'call'
'''