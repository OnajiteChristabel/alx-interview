#!/usr/bin/python3
'''Prime Game'''

def isWinner(num_rounds, num_list):
    '''Finds the winner'''
    winners_count = {'Maria': 0, 'Ben': 0}

    for i in range(num_rounds):
        round_winner = determine_round_winner(num_list[i], num_rounds)
        if round_winner is not None:
            winners_count[round_winner] += 1

    if winners_count['Maria'] > winners_count['Ben']:
        return 'Maria'
    elif winners_count['Ben'] > winners_count['Maria']:
        return 'Ben'
    else:
        return None

def determine_round_winner(n, num_rounds):
    '''Determine the round winner'''
    num_range = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        current_player = players[i % 2]
        selected_indices = []
        prime = -1

        for idx, num in enumerate(num_range):
            if prime != -1:
                if num % prime == 0:
                    selected_indices.append(idx)
            else:
                if is_prime(num):
                    selected_indices.append(idx)
                    prime = num

        if prime == -1:
            if current_player == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(selected_indices):
                del num_range[val - idx]
    return None

def is_prime(n):
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n**(1/2)) + 1, 2):
            if n % i == 0:
                return False
        return True

