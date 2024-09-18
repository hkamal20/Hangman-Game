#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 16:28:01 2023

@author: haniya
"""



## Below are several functions that collectively implement a fully functional hangman game

import random

WORDLIST_FILENAME = "words.txt" #file with different words that program will pull from

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord (str): The word the player is trying to guess.
    lettersGuessed (list): A list of letters that have been guessed so far.
    
    Returns False until all the letters are guessed correctly in secretWord
    """
    
    for n in secretWord:
        if n not in lettersGuessed: 
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord (str): The word the player is trying to guess.
    lettersGuessed (list): A list of letters that have been guessed so far.
    
    Returns the word with guessed letters filled in and unguessed letters as '_'
    """
    word = ''
    for n in secretWord:
        if n in lettersGuessed:
            word += n
        else:
            word += '_ '
    return word

def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed (list): A list of letters that have been guessed so far.
    
    Returns the letters that have not been guessed yet
    """
    import string
    alphabet = string.ascii_lowercase
    list1 = list(alphabet)
    
    for n in lettersGuessed:
        list1.remove(n)
        
    return ''.join(list1)

def hangman(secretWord):
    lettersGuessed = []
    i = 8  # Number of guesses player has

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')

    while i > 0 and isWordGuessed(secretWord, lettersGuessed) == False:
        print('-------------')
        print('You have ' + str(i) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ').lower()

        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))

            if isWordGuessed(secretWord, lettersGuessed) == True:
                break

        elif guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))

        else:
            lettersGuessed.append(guess)
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            i -= 1

    if i == 0:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.')
    else:
        print('-------------')
        print('Congratulations, you won!')

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)







