import random
guess = ''
coinSides = ['heads', 'tails']
while guess not in coinSides:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = coinSides[random.randint(0, 1)] # 0 is tails, 1 is heads
# Bug1: comparing an int to a string
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    # Bug2: misspelling variable name
    guess = input()
    if toss == guess:
        print('You goit it!')
    else:
        print('Nope.You are really bad at this game.')
