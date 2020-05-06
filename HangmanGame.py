import random

words_dict = {
  1: "rorschach",
  2: "privacy",
  3: "manhattan",
  4: "interstellar",
  5: "coffee",
  6: "ozymandias",
  7: "mandalorian",
  8: "jenga",
  9: "dimensional",
  10: "invitctus",
  11: "comedian",
  12: "mission",
  13: "sportage",
  14: "brooklyn",
  15: "anxiety",
  16: "genetic",
  17: "prince",
  18: "storm",
  19: "common",
  20: "threat",
}

hangman_body = ["""
  _______
  |     |
  |     
  |    
  |    
  |
 _|_______""",
 """\
  _______
  |     |
  |     0
  |    
  |    
  |
 _|_______""",
 """\
  _______
  |     |
  |     0
  |     |
  |    
  |
 _|_______""",
 """\
  _______
  |     |
  |     0
  |    /|
  |    
  |
 _|_______""",
 """\
  _______
  |     |
  |     0
  |    /|\ 
  |    
  |
 _|_______""",
 """\
  _______
  |     |
  |     0
  |    /|\ 
  |    / 
  |
 _|_______""",
 """\
   _______
  |     |
  |     0
  |    /|\ 
  |    / \  
  |
 _|_______
 """]


def display_game(hangman_body, missed_letter, correct_letters, secret_word):
  print(hangman_body[(len(missed_letter)- 1)])
  blank_spaces = ("_" * (len(secret_word)))

  for i in range(len(secret_word)):
    if secret_word[i] in correct_letters:
      blank_spaces = blank_spaces[:i] + secret_word[i] + blank_spaces[i+1:]
  
  for letter in blank_spaces:
    print(letter, end=" ")
pass

def get_guess(letters_guessed):

  while True:
    print("\nYou have",attempts,"wrong chances remaining")
    print("\nLetters previously used:",(correct_letters + missed_letters))
    user_guess = input("\nGuess a letter: ")
    if len(user_guess) > 1:
      print("Please enter 1 letter at a time please.")
    elif (user_guess.isalpha() == False):
      print("Please enter a letter between A-Z.")
    elif user_guess in letters_guessed:
      print(" You have already tried that letter")
    else: 
      return user_guess
pass

def welcome_screen():
   print(""" 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
   """)
   print("Welcome to HANGMAN!!")
   print("In this game you are required to guess a word chosen by random which will appear as blank spaces. You must guess the word one letter at a time. Each time you guess a correct letter, that letter is revealed. On the other hand, each incorrect letter adds a body part to the gallow. If a full body appears in the gallow, you're dead, and it means you ran out of chances. GOOD LUCK and THANKS FOR PLAYING!")
pass

def play_game():
  print(welcome_screen())
  global attempts, correct_letters, missed_letters
  missed_letters = " "
  correct_letters = " "
  secret_word = words_dict[random.randint(1, (len(words_dict)))]
  attempts = (len(hangman_body)-1)
  
  while (attempts > 0):
    display_game(hangman_body, missed_letters, correct_letters, secret_word)

    user_guess = get_guess((missed_letters + correct_letters))

    if user_guess in secret_word:
      correct_letters = correct_letters + user_guess

      found_all = True
      for i in range(len(secret_word)):
         if secret_word[i] not in correct_letters:
           found_all = False
           break
    
      if found_all:
        print("The word was",secret_word,"! You WON!!!!")
        print("Do you want to play again?")
        reply = input("Yes or No? ").lower()
        if (reply == "yes"):
          print(play_game())
        else: 
          return("Thanks for playing!!")
    else:
      missed_letters += user_guess
      attempts -= 1
  display_game(hangman_body, missed_letters, correct_letters, secret_word)
  print("\nYou ran out of attempts")
  print("The word was",secret_word,)
  print("Do you want to play again?")
  reply = input("Yes or No? ").lower()
  if (reply == "yes"):
    print(play_game())
  else:
    return("Thanks for playing!!")
pass

print(play_game())