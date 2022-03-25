from random import randint as rndi
from time import sleep as slp

def game():
    number : int = int ( input('Enter a number from 1 to 100, for the computer to guess: ') )
    # print (number)
    
    initial = 1
    final = 100
    guess_number : int = rndi(initial,final)
    print (guess_number)
    
    while True:
        if number == guess_number:
            print (f'You guessed the number ({number}), Congratulations!')
            break
        elif number < guess_number:
            print ('The correct number is lower, try again...')
            final = guess_number - 1
            guess_number : int = rndi(initial,final)
        else:
            print ('The correct number is greater, try again...')
            initial = guess_number + 1
            guess_number : int = rndi(initial,final)
        print (guess_number)
        slp(1)


if __name__ == '__main__':
    game()