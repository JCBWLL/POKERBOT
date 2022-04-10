def play(player, flop, current_bet, players_still_in, is_first_round):

    if current_bet == 10:
        return 'call'
    else:
        return 'fold'
#no
# return formatting:
# for fold, return 'fold'
# for raise, return 'raise {amount}' e.g 'raise 10'
# for call, return 'call'