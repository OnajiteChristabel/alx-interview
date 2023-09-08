def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def compute_primes(limit):
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def play_round(n, primes):
    remaining_numbers = set(range(1, n + 1))
    maria_turn = True
    
    while True:
        valid_move = False
        for prime in primes:
            if prime in remaining_numbers:
                valid_move = True
                remaining_numbers -= set(range(prime, n + 1, prime))
                maria_turn = not maria_turn
                break
        
        if not valid_move:
            break
    
    return "Maria" if maria_turn else "Ben"

def isWinner(x, nums):
    primes = compute_primes(1000)
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_round(n, primes)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
