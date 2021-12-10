import random
NumberRandom = random.randint(0,100)

while True:
    Guess = int(input('Enter your  first guess number: '))
    if Guess == NumberRandom:
        print ('Correct')
        break
    if Guess >= NumberRandom:
        print ('Your guess is too high')
    if Guess <= NumberRandom:
        print ('Your guess is too low')