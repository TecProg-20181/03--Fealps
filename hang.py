# -*- coding: UTF-8 -*-
import random
import string

WORDLIST_FILENAME = "palavras.txt"


def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    #check if file exist
    try:
        # inFile: file
        inFile = open(WORDLIST_FILENAME, 'read', 0)
    except IOError:
       print "Error: File does not appear to exist. Exiting program"
       quit()
    inFile = open(WORDLIST_FILENAME, 'read', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    print
    print
    print
    print
    print
    print
    print
    print
    print
    print
    print
    print
    return random.choice(wordlist)

#check if the word was guessed
def isWordGuessed(secretWord, letters_guessed):
    secret_Letters = []
    for letter in secretWord:
        if letter in letters_guessed:
            pass
        else:
            return False
    return True

def get_available_letters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase
    return available

# This function counts how many letters the word has and warn you how many different letters there are in the word.
def count_letters(secretWord):
    letters = []
    for letter in secretWord:
        if letter not in letters:
            letters.append(letter)
    return len(letters)

# This function validates if the word has different letters have the same size as the attempts, and if its not empty.
def validated_word (secretWord, guesses):

    validated_word = False

    while not validated_word:
        unique_letters = count_letters(secretWord)
        if len(secretWord) < 0:
            secretWord = reloadWords()
        elif guesses < unique_letters:
            print 'The secret Word have too many unique letters, reloading the letters'
            secretWord = reloadWords()
        else:
            print 'There are', unique_letters, 'unique Letters in this word'
            validated_word = True
    return secretWord

#this function reloads the secret word in case it fails the validate check function
MAXIMUM_TRIES = 20
TRIES = 0
def reloadWords():
    secretWord = loadWords()
    TRIES += 1
    if TRIES >= MAXIMUM_TRIES:
        print'Reached maximum amount of tries, exiting program'
        return None
    else:
        return secretWord

def guessed_letters(secretWord, letters_guessed):
    guessed = ''
    for letter in secretWord:
        if letter in letters_guessed:
            guessed += letter
        else:
            guessed += '_ '
    return guessed

def show_available_letters(letters_guessed):
    available = get_available_letters()
    for letter in available:
        if letter in letters_guessed:
            available = available.replace(letter, '')
    print 'Available letters', available

def hangman(secretWord):
    guesses = 8
    letters_guessed = []

    print 'You were gibbet!, your executioner propose a game.'
    print 'If you guess the word he is thinking, he agrees to let you live'
    print 'You start with 8 guesses'
    print 'with a hoarse voice the executioner speaks: '
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    secretWord = validated_word(secretWord, guesses)
    if secretWord == None:
        return

    print '-------------'

    while  isWordGuessed(secretWord, letters_guessed) == False and guesses >= 0:
        if guesses > 0:
            print 'You have ', guesses, 'guesses left.'
        else:
            print 'Last Chance'

        show_available_letters(letters_guessed)
        letter = raw_input('Please guess a letter: ')
        letter =letter.lower()
        if len(letter) <= 0:
            print 'Sorry, what did you say?'

        elif letter.isalpha() == False:
            print 'I am working with letters'

        elif len(letter) > 1:
            print 'Only one letter per guess'

        elif letter in letters_guessed:
            guessed = ''
            guessed = guessed_letters(secretWord, letters_guessed)
            print 'Oops! You have already guessed that letter: ', guessed

        elif letter in secretWord:
            letters_guessed.append(letter)
            guessed = ''
            guessed = guessed_letters(secretWord, letters_guessed)
            print 'Good Guess: ', guessed

        else:
            guesses -=1
            letters_guessed.append(letter)
            guessed = ''
            guessed = guessed_letters(secretWord, letters_guessed)
            print 'Oops! That letter is not in my word: ',  guessed

        print '------------'

    else:
        if isWordGuessed(secretWord, letters_guessed) == True:
            print 'Correct, you are now free to go!'
        else:
            print 'Sorry, you ran out of guesses. The word was', secretWord, '.'
            print 'You Died.'

secretWord = loadWords().lower()
hangman(secretWord)
