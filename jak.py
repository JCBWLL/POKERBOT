def play(player, flop, current_bet, players_still_in):

    if current_bet == 10:
        return 'call'
    else:
        return 'fold'
#no
# return formatting:
# for fold, return 'fold'
# for raise, return 'raise {amount}' e.g 'raise 10'
# for call, return 'call'