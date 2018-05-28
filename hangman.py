# Hangman game
# 電腦從word.txt這個字庫中隨機抽選一個字，玩家一次猜一個字母，有八次機會
import random

WORDLIST_FILENAME = "words.txt"
#重要！請把words.txt放置與此程式同一路徑下

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

# end of helper code
# -----------------------------------



def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    count = 0
    for letter in lettersGuessed:
        if letter in secretWord:
            count+=1
    return count == len(secretWord)

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    answer = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            answer += letter
        else:
            answer += '_ '
    return answer        



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in lettersGuessed:
        if letter in alphabet:
            alphabet.remove(letter)
    ans = ''
    for letter in alphabet:
        ans += letter
    return ans
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    
    numOfLet = 0 
    for letters in secretWord:
        numOfLet += 1 
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' +str(numOfLet) + ' letters long.')
    '''
    guess start
    '''
    guessTimes = 8
    lettersGuessed = []
    availableLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    while isWordGuessed(secretWord, lettersGuessed) is False and guessTimes > 0:
        print('You have '+ str(guessTimes)+ ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        x = input('Please guess a letter: ')
        
        if x in secretWord:
            if x in lettersGuessed:
                print ("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(x)
                print ('Good guess: '+ getGuessedWord(secretWord, lettersGuessed))
                
        else:
            lettersGuessed.append(x)
            print ("Oops! That letter is not in my word: "+getGuessedWord(secretWord, lettersGuessed))
            guessTimes -= 1
    if isWordGuessed(secretWord, lettersGuessed) is True:
         print('Congratulations, you won!')
    else:
         print('Sorry, you ran out of guesses. The word was else.')

import random

secretWord = chooseWord(loadWords())
hangman(secretWord)

