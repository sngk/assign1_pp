# Name:				Andrew
# Date:				21/08/2018

# This file is provided to you as a starting point for the "word_game.py" program of Assignment 1
# of CSP1150/CSP5110 in Semester 2, 2018.  It mainly provides you with a suitable list of words.
# Please use this file as the basis for your assignment work.  You are not required to reference it.

# Import the random module to allow us to select the word list and password at random.
import random
# import the betterInput module to check whether input is correct or not (i.e. numbers should be between 1 and 8 only etc.)
import betterInput

# ''' Global variables:
# 		candidateWords		Create a list of 100 words that are similar enough to work well for this game
# 		guessesRemaining 	integer stores the number of gusses user can use to guess the word
# 		won			boolean defines if we need to continue the loop or not
# 		wordList			list of generated "passwords" from the list of given words candidateWords
# 		password			stores one element from the list of generated words wordList
# 		guessedWords		stores the history of words that user entered as their guess. 
# 							Actually it stores correct number of letters in that word not the word itself
# '''
candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES', 'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER',
                  'GELDED', 'GELDER', 'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR', 'TEENER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDED', 'WEEDED', 'WELDED', 'YONDER']
guessesRemaining = 0
won = False
wordList = random.sample(candidateWords, 8)
password = random.choice(wordList)
guessedWords = ['', '', '', '', '', '', '', '']

'''	generateWords() function to generate words from the given list
	wordList	stores the list of generated words
	return		list of words
'''


def generateWords():
    global wordList
    wordList = random.sample(candidateWords, 8)
    return wordList

# generatePwd() function to generate a password from the list of generated words
# return password


def generatePwd():
    global password
    password = random.choice(wordList)
    return password


'''
	choiceGameDifficulty() function asks user to choose game difficulty from
	four possible options: 	easy with 4 tries to guess the password
							medium - 3 guesses
							hard - 2 guesses
							insane - 1 guess (just to test your luck hehe)
'''


def choiceGameDifficulty(question, errorMessage='Invalid input - Try again. \nUse the following words: Easy, Medium, Hard, Insane'):
    while True:
        global guessesRemaining
        value = input('%s[Easy, Medium, Hard, Insane]' % question).lower()
        try:
            response = value
            print (response)
            if response == 'easy':
                guessesRemaining = 4
                break
            if response == 'medium':
                guessesRemaining = 3
                break
            if response == 'hard':
                guessesRemaining = 2
                break
            if response == 'insane':
                guessesRemaining = 1
                break
            else:
                print (errorMessage)
                continue
        except ValueError:
            print(errorMessage)
            continue


'''	continueGame() is the function to check if user wants to start a new game
	return	true if user wants to start a new game
				and set all global variables to default
				as well as generate new set of words and password;
			false if user doesn't want to start a new game
'''


def continueGame():
    global guessedWords, guessesRemaining, wordList, password
    startNewGame = betterInput.choiceQuestionYesNo('Would you like to start a new game?')
    if startNewGame == False:
        return False
    else:
        guessedWords = ['', '', '', '', '', '', '', '']
        wordList = generateWords()
        password = generatePwd()
        choiceGameDifficulty('Please choose the difficulty ')
        welcomeMsg()
        return True


'''	The following function compares two given words and returns the number of matching letters
	correct		integer stores number of matching letters between chosen "password" and enterd word
'''


def compareWords(word1, word2):
    correct = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            correct += 1
    return correct


def printList():
    for counter, word in enumerate(wordList, 1):
        print (''.join('{}) {} {param}'.format(counter, word, param=guessedWords[counter - 1])))


'''	welcomeMsg() function is basically a welcome message. It'll show up whenever the new game starts.
	The first line of this function is my attempt to "clear" the shell screen somehow. 
	Unfortunately, IDLE can't do it using more efficient way '''


def welcomeMsg():
    print ('\n' * 50)
    print (f'Welcome to the Guess-The-Word game! \nYou can see 8 words, and you have to guess the correct one.\nYou only have {guessesRemaining} guesses.\nPassword is one of the words: ')
    printList()


'''
	main() function where magic happens :D
'''


def main():
    global won, guessesRemaining, wordList, password, guessedWords
    choiceGameDifficulty('Please choose the difficulty ')
    welcomeMsg()
    while not won:
        print ('Guesses remaining: ', guessesRemaining)
        guess = betterInput.inputInteger('Enter your guess > ', minValue=1, maxValue=8)
        guessesRemaining -= 1
        print('> ', wordList[guess - 1])
        correct = compareWords(wordList[guess - 1], password)
        guessedWords[guess - 1] = str(correct) + '[/6 correct]'  # list stores number of corrcet letters

        if wordList[guess - 1] == password:
            print ('Password correct! Congrats!')
            newGame = continueGame()
            if newGame == False:
                won = True
            else:
                won = False
        elif guessesRemaining <= 0:
            printList()
            print ('You lost, because you do not have more guesses. \nGame Over!')
            newGame = continueGame()
            if newGame == False:
                won = True
            else:
                won = False
        else:
            printList()
            continue


# runs the program
main()
