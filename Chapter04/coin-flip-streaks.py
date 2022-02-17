import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that checks if there is a streak of 6 heads or tails in a row in 100 flips.
    heads = 0
    for _ in range(100):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            heads = 0
        if heads == 6:
            numberOfStreaks += 1
            heads = 0

print(f"Chance of streak: {numberOfStreaks / 100}")
