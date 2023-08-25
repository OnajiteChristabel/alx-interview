#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins required to reach
    a specified total amount.
'''
import sys

def minCoins(coins, target):
    '''
    Return: minimum number of coins required to reach the target amount.
    If the target is 0 or less, return 0.
    If the target cannot be reached using the available coins, return -1.
    '''
    if target <= 0:
        return 0
    
    inf = sys.maxsize
    dp = [inf] * (target + 1)
    dp[0] = 0
    
    numCoins = len(coins)
    for i in range(1, target + 1):
        for j in range(numCoins):
            if coins[j] <= i:
                subResult = dp[i - coins[j]]
                if subResult != inf and subResult + 1 < dp[i]:
                    dp[i] = subResult + 1
    
    if dp[target] == inf:
        return -1
    return dp[target]

# Example usage
if __name__ == "__main__":
    coins = [1, 2, 5]
    target = 11
    result = minCoins(coins, target)
    if result == -1:
        print("Cannot reach the target amount.")
    else:
        print("Minimum number of coins required:", result)
