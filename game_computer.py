from random import randint as rndi
from time import sleep as slp

def game():
    while True:
        try:
            number : int = int ( input('Enter a integer number from 1 to 100, for the computer to guess: ') )
            break
        except ValueError:
            print ('Incorrect value, try again')
    
    initial = 1
    final = 100
    guess_number : int = rndi(initial,final)
    print (guess_number)
    count = 1

    while True:
        if number == guess_number:
            print (f'Computer guesses the number ({number}) in {count} attemps')
            break
        elif number < guess_number:
            print ('The correct number is lower, try again buddy...')
            final = guess_number - 1
            guess_number : int = rndi(initial,final)
        else:
            print ('The correct number is greater, try again buddy...')
            initial = guess_number + 1
            guess_number : int = rndi(initial,final)
        print (guess_number)
        slp(1)
        count += 1


if __name__ == '__main__':
    game()