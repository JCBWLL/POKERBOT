import random
import coon
import cob
import jak

CARD_ORDER = '1234567890JQKA'
SUITS = 'DCHS'

DECK = []
for card in CARD_ORDER:
    for suit in SUITS:
        DECK.append(card + suit)

def deal_cards(DECK, PLAYERS):
    random.shuffle(DECK)

    for player in PLAYERS:
        i = 0
        while i < 2:
            player['hand'].append(DECK[i])
            DECK.pop(i)
            i = i+1

number_of_players = 3
players = []
flop = []

for i in range(1,number_of_players+1):
    name = 'Player ' + str(i)
    hand = []
    funds = 50
    players.append({'name': name, 'hand': hand, 'funds': funds, 'current_bet': 10, 'still_in': True, 'previous_play': '',})

play_functions = [coon.play, jak.play, cob.play]
random.shuffle(play_functions)
for player in players:
    player['play'] = play_functions[0]
    play_functions.pop(0)

deal_cards(DECK, players)

print('\nThe game has begun.')
i = 0

players[0]['current_bet'] = 5
players[0]['funds'] -= 5
players[1]['current_bet'] = 10
players[1]['funds'] -= 10

current_bet = 10
pot = 15

players.insert(0, players.pop())


active_players = players.copy()

for player in players:

    play = player['play'](player, [], 10, 3)
    print(player['name'], 'has played:', play)
    if play.split(' ')[0] == 'raise':
        play = play.split(' ')
        if int(play[1]) > funds:
            print("player doesnt have sufficent funds")
            quit()
        player['funds'] -= int(play[1]) + 10
        pot += int(play[1])
        player['current_bet'] = player['current_bet'] + int(play[1])
        current_bet += int(play[1])
        print('The current bet is now:', current_bet)
        

    elif play == 'call':
        if current_bet > funds:
            print("player doesnt have sufficent funds")
            quit()
        player['funds'] -= (current_bet - player['current_bet'])
        pot += (current_bet - player['current_bet'])
        player['current_bet'] = player['current_bet'] + (current_bet - player['current_bet'])
        
        
    elif play == 'fold':
        active_players.remove(player)
    
    print(player['funds'])
    print(player['current_bet'])

players = active_players

i = 0
flop = []
while i < 3:
    flop.append(DECK[i])
    DECK.pop(i)
    i += 1
print(flop)
while len(flop) < 5:
    if len(players) == 1:
        print(players[0]['name'],'has won!\n')
        break
    
    
    for player in players:
        play = player['play'](player, [], 10, 3)
        print(play)
        if play.split(' ')[0] == 'raise':
            play = play.split(' ')
            if int(play[1]) > funds:
                print("player doesnt have sufficent funds")
                quit()
            player['funds'] -= int(play[1])
            pot += int(play[1])
            player['current_bet'] = player['current_bet'] + int(play[1])
            current_bet += int(play[1])
            print('The current bet is now:', current_bet)

        elif play == 'call':
            if current_bet > funds:
                print("player doesnt have sufficent funds")
                quit()
            player['funds'] -= (current_bet - player['current_bet'])
            pot += (current_bet - player['current_bet'])
            player['current_bet'] = player['current_bet'] + (current_bet - player['current_bet'])
            
            
        elif play == 'fold':
            active_players.remove(player)
    #print(players)
    flop += [DECK[0]]
    DECK.pop(0)
