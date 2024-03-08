#!/usr/bin/python3
'''
Given a pile of coins of different values,
determine the fewest number of coins needed to meet
a given amount total.
'''
def makeChange(coins, total):
    '''
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
        return 0

    # Initialize dp array with total+1 as we can't have more coins than total+1
    dp = [total+1]*(total+1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total+1):
            dp[amount] = min(dp[amount], dp[amount-coin] + 1)

    return dp[total] if dp[total] != total+1 else -1

