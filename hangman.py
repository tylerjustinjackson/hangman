import random
from wordbank import wordbank

pastmoves = []

wordboard = []

var1 = '''
  _____
  |   |
  |   O
  |  /|\\
  |   |
  |  / \\
_____'''
var2 = '''
  _____
  |   |
  |   O
  |  /|\\
  |   |
  |  /
_____'''
var3 = '''
  _____
  |   |
  |   O
  |  /|\\
  |   |
  |   
_____'''
var4 = '''
  _____
  |   |
  |   O
  |  /|
  |   |
  |   
_____'''
var5 = '''
  _____
  |   |
  |   O
  |   |
  |   |
  |   
_____'''
var6 = '''
  _____
  |   |
  |   O
  |  
  |   
  |   
_____'''
var7 = '''
  _____
  |   |
  |   
  |  
  |   
  |   
_____'''
currentlife = [var7, var6, var5, var4, var3, var2, var1]


# GLOBAL FUNCTIONS
def startboard():  # created blank board same length as random word
    for i in range(0, len(word)):
        wordboard.insert(i, '_')


def printboard():  # prints current board
    for i in range(0, len(word)):
        print(f'{wordboard[i]}  ', end='')
    print('')


def newword():  # created new random word from stored list
    word = wordbank[random.randint(0, len(wordbank)-1)]
    return word


def tryagain():  # asks user if they would liek to try game again
    x = input('Would you like to try again? ').strip().lower()
    if x == 'yes' or x == 'y':
        return True
    else:
        return False


def usermove(word):  # main gameplay function
    lives = 0

    while True:

        x = input("Please input a letter: ").lower().strip()  # move input

        if len(x) == 1:  # makes sure user inputted one character only
            if x.isalpha():  # makes sure user inputted alphabetical character only
                if x in word:
                    # loops over every letter and find if letter matches and places it on board if so
                    for n in range(0, len(word)):
                        if word[n] == x:
                            wordboard[n] = x
                    # prints digital art of hangman based on how many lives are left
                    print(currentlife[lives])
                    print('')
                    printboard()

                elif x not in word:  # if letter not in word, subtracts a life
                    lives += 1
                    print('You just lost one of your lives')
                    print(currentlife[lives])

                    if lives == (len(currentlife)-1):  # out of lives? game over
                        print('Game Over! No more lives!')
                        print(f'The correct answer was {word}')
                        break
                    printboard()

                if '_' not in wordboard:  # if board is full
                    print('Congrats! You won!')  # you win
                    break

            else:  # exception handling
                print('Please only input alphabetical values')
        else:  # exception handling
            print('You inputted too many characters. Please retry!')


if __name__ == '__main__':
    try:
        while True:
            print('')
            word = newword()  # makes new word
            startboard()  # starts game
            usermove(word)  # starts main gameplay
            z = tryagain()  # want to try again?
            if z == True:  # if yes, continue
                print('')
                continue
            elif z == False:  # if no, BYE!
                break

    except:
        pass
