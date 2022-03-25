from random import randint as rndi
from time import sleep as slp

def game():
    number: int = rndi(1,100)
        
    while True:
        guess_number: int = int( input('Enter a number from 1 to 100: ') )
        if number == guess_number:
            print (f'You guessed the number ({number}), Congratulations!')
            break
        elif number < guess_number:
            print ('The correct number is lower, try again...')
        else:
            print ('The correct number is greater, try again...')
        slp(1)


if __name__ == '__main__':
    game()