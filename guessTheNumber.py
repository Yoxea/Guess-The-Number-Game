import random

print('Hello, What is your name?')
name = input()

print('Welcome ' + name + '!')
print('====================================')
print('A number is chosen, between 1 to 100')
print('Guess the number')
print('within 7 trials')
print('====================================')

number = random.randint(1, 100)

for guessTaken in range(0, 7):
    print('Guess the number:')
    guess = int(input())
    
    if guess < number:
        print('The number is higher than ' + str(guess))

    elif guess > number:
        print('The number is lower than ' + str(guess))
    else:
        break
        

if guess == number:
    print('Congratulations ' + name + '! you have guessed the right number ' + 'after ' + str(guessTaken) + ' guesses!')
else:
    print('You have exhausted your trials ' + name + ', the number was ' + str(number))