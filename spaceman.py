import random

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#ascii art for spaceman
spaceman = []
spaceman.append('        _..._\n')
spaceman.append('      .'     '.      _\n')
spaceman.append('     /    .-""-\   _/ \ \n')
spaceman.append('   .-|   /:.   |  |   |\n')
spaceman.append("   |  \  |:.   /.-'-./ \n")
spaceman.append("   | .-'-;:__.'    =/\n")
spaceman.append("   .'=  *=|NASA _.='\n")
spaceman.append('  /   _.  |    ;\n')
spaceman.append(" ;-.-'|    \   |\n")
spaceman.append("/   | \    _\  _\ \n")
spaceman.append("\__/'._;.  ==' ==\ \n")
spaceman.append("         \    \   |\n")
spaceman.append('         /    /   /\n')
spaceman.append('         /-._/-._/\n')
spaceman.append('         \   `\  \ \n')
spaceman.append('          `-._/._/\n')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word
#storing the secret word here for global use
secret_word = load_word()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#store answers as list globally
correct = []
false = []
def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    if guess in secret_word:
      correct.append(guess)
      return True
    else:
      false.append(guess)
      return False

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#user input
def guess_a_letter():
  guess = input('Guess a letter  -->  ')
  if len(guess) > 1:
      print("Guess one letter at a time please!")
      guess = input('Guess a letter  -->  ')
  for guesses in range(len(correct)):
      if guess == correct[guesses]:
          print(f"You already guessed {guess}, guess again!")
          guess = input('Guess a letter  -->  ')
  for guesses in range(len(false)):
    if guess == false[guesses]:
        print(f"You already guessed {guess}, guess again!")
        guess = input('Guess a letter  -->  ')
  return guess
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#prints the correctly guessed letters
#storing lists outside the loop so that they save letters
letters = list(secret_word)
print(letters)
guessed_word = []
def get_guessed_word(secret_word, guess):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters that have been guessed in the current loop.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    for i in range(len(letters)):
        if len(guessed_word)<len(letters):
            guessed_word.append("_")
    

    for i in range(len(letters)):
        if guess == letters[i]:
            guessed_word[i] = letters[i]
    print(guessed_word)

    pass

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def is_word_guessed(guessed_word, letters):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        letters (list of strings): the random word the user is trying to guess in a list of letters.
        guessed_word (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: False only if all the letters of secret_word are in letters_guessed or if user runs out of guesses, True otherwise
    '''
    if guessed_word == letters or len(false) > 6:
        return False
    else:
        return True

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def draw_spaceman():
    wrong = 0
    if len(false) > wrong:
        for i in range(3*len(false)):
            if(i < len(spaceman)):
                print(spaceman[i])
            elif(i > len(spaceman)):
                print("Last Guess!")
        wrong+=1


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
def game():
   '''
   A function that controls the game of spaceman. Will start spaceman in the command line.
   '''
   print("_____________________ WELCOME TO SPACEMAN _____________________\n")
   print("How to play:\n")
   print("A secret word will be chosen at random for you to guess.\n")
   print("Guess letters, one at a time, when prompted in the command line.\n")
   print("If you guess the word before the spaceman is drawn and comes for you, you win!\n")
   print("________________________________________________________________")
   running = True
   while running == True:
       draw_spaceman()
       guess = guess_a_letter()
       is_guess_in_word(guess, secret_word)
       get_guessed_word(secret_word, guess)
       running = is_word_guessed(guessed_word, letters)
   if len(false) > 6:
       print(f"The correct word was:\n{letters}\n\n\n\n\n")
   else:
       print("Congrats, you won!")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

game()