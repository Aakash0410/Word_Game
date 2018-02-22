# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string



WORDLIST_FILENAME = "words.txt"



def loadWords():
    """gfh
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

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
   
    l2=[]
    for k in secretWord:
        if k in lettersGuessed:
            l2.append(k)
           
    if(len(l2)==len(secretWord)):
     return True
                 
               
            
            
     
    
         
 

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    str=""
    flag=0
    
    for k in secretWord :
         if k in lettersGuessed:
             str=str+k
             if k in lettersGuessed[-1]:
           
            
                  flag=1
           
         else:
            str=str+'_'
           
    if(flag==1):
        
         s=str

    else:
        s=str
       
    
      
    return s  


  
    
    
    
    
    
    
       
        
            



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    k=(string.ascii_lowercase)
    str=""
    for s in k:
     if s not in lettersGuessed:
        str=str+s
    return str
        
        

def hangman(secretWord):
    total=8
    print("Welcome to the game,Hangman!")
    print("I am thinking of a word that is",len(secretWord), "letters long" )
    print("-------------------------------------")
    lettersGuessed=[]
    while(total>0):
     print("You have" ,total," guesses left")
     print("Available letters are:" +getAvailableLetters(lettersGuessed))
     h=input("Please guesss a letter:")
   
     
     if  h in lettersGuessed:
         s1=("Oops! You've already guessed that letter:"+getGuessedWord(secretWord, lettersGuessed)) 
         print(s1)
        
     else:
         lettersGuessed.append(h)
         right=getGuessedWord(secretWord,lettersGuessed)
         
         if h in secretWord:
           print("Good guess:" +right)
         else:
           print("oops that letter is not in my word:"+right)
           
           total -=1
     print("------------------------------------")
     right1=isWordGuessed(secretWord, lettersGuessed)
     if(right1==True):
      print("Congratulation,you won")
      break
      
     if(total==0):
      print("Sorry, you ran out of guesses. The word was " +secretWord) 
      
     
        
   
    
    
     
    





secretWord = "aakash"
hangman(secretWord)
