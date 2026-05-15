import random

title = r'''
 .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |
| | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |
| |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |
| |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |
| |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |
| | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
'''
print(title)
print("Welcome to Hangman!, for this game you will have to guess the word by guessing the letters in the word, you have 6 chances to guess the word, good luck!")

word_dict = ['python', 'hangman', 'challenge', 'programming', 'developer', 'algorithm', 'function', 'variable', 'iteration', 'recursion', 'object', 'class', 'inheritance', 'polymorphism', 'encapsulation', 'abstraction', 'data', 'structure', 'array', 'list', 'dictionary', 'tuple', 'set', 'string', 'integer', 'float', 'boolean', 'loop', 'condition', 'exception', 'file', 'input', 'output', 'debugging', 'testing', 'version', 'control', 'git', 'github', 'bitbucket', 'gitlab', 'docker', 'kubernetes', 'cloud', 'aws', 'azure', 'google', 'cloud', 'computing', 'machine', 'learning', 'artificial', 'intelligence', 'deep', 'learning', 'neural', 'network', 'data', 'science', 'big', 'data', 'analytics', 'visualization', 'business', 'intelligence', 'sql', 'database', 'nosql', 'mongodb', 'mysql', 'postgresql', 'sqlite', 'redis', 'cassandra', 'hadoop', 'spark', 'scala', 'java', 'javascript', 'typescript', 'ruby', 'rails', 'php', 'laravel', 'symfony', 'django', 'flask']

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word = random.choice(word_dict)
unique_letters = set(word)
lives = 6
user_word = '_' * len(word)
user_inputs = set()

while lives > 0:
    print(HANGMANPICS[6 - lives])
    print(f"word: {user_word}")
    print(f"Remaining lives: {lives}")
    guess = input("guess a letter: ").lower()

    if guess in user_inputs:
        print("You already guessed that letter!")
        continue

    user_inputs.add(guess)

    if guess in word:
        print("correct!\n")
        unique_letters.remove(guess)
    else:
        print("incorrect!\n")
        lives -= 1
    
    for i in range(len(word)):
        if word[i] == guess:
            user_word = user_word[:i] + guess + user_word[i+1:]
            
    if len(unique_letters) == 0:
        print(f"Congratulations! You guessed the word: {word}")
        quit()

print(f"Game over! The word was: {word}")