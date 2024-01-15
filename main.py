import random
import os
from word_list import words
from termcolor import colored

def main():
  # Clear terminal output for a better game experience
  os.system('cls||clear')

  secret_word = random.choice(words).upper()
  word_completion = "_" * len(secret_word)

  has_guessed = False
  guessed_letters = []
  wrongly_guessed_letter = []
  guessed_words = []
  retries = 8

  while not has_guessed and retries > 0:
    guess = input("Please guess a letter or word: ").upper()

    # Clear terminal output for a better game experience
    os.system('cls||clear')

    # If the player is guessing a letter
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print(colored(f"You already guessed the letter {guess}", "red"))
      elif guess not in secret_word:
        print(colored(f"{guess} is not in the word.", "magenta"))
        retries -= 1
        guessed_letters.append(guess)
        wrongly_guessed_letter.append(guess)
      else:
        print(colored(f"Good job, {guess} is in the word!", "green"))
        guessed_letters.append(guess)

        # Convert to a list
        word_as_list = list(word_completion)

        # Find the index of the matching letter in the word
        indices = [i for i, letter in enumerate(secret_word) if letter == guess]
        for index in indices:
          word_as_list[index] = guess
        word_completion = "".join(word_as_list)

        # Win if no letter left to guess
        if "_" not in word_completion:
          has_guessed = True

    # If the player is guessing the whole word
    elif len(guess) == len(secret_word) and guess.isalpha():
      if guess in guessed_words:
        print(colored(f"You already guessed the word {guess}", "red"))
      elif guess != secret_word:
        print(colored(f"{guess} is not the word.", "magenta"))
        retries -= 1
        guessed_words.append(guess)
      else:
        has_guessed = True
        word_completion = secret_word
    else:
        print(colored("Not a valid guess.", "red"))

    print(colored(display_output(retries), "cyan"))
    print(f"Wrong letters and words you have guessed: {colored(', '.join(wrongly_guessed_letter + guessed_words), 'red', attrs=['underline'])}\n")
    print(f"The secret word: {colored(word_completion, 'green', attrs=['bold'])}\n")
  if has_guessed:
    print("Congrats, you guessed the word! You win!")
  else:
    print("Sorry, you ran out of retries. The word was " + colored(secret_word, "yellow") + ". Maybe next time!")


def display_output(retries_left):
  stages = [
    """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
    """,
    """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / 
        -
    """,
    """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |      
        -
    """,
    """
        --------
        |      |
        |      O
        |     \\|
        |      |
        |     
        -
    """,
    """
        --------
        |      |
        |      O
        |      |
        |      |
        |     
        -
    """,
        """
        --------
        |      |
        |      O
        |      |
        |      
        |     
        -
    """,
    """
        --------
        |      |
        |      O
        |    
        |      
        |     
        -
    """,
    """
        --------
        |      |
        |      
        |    
        |      
        |     
        -
    """,
    """
        --------
        |      
        |      
        |    
        |      
        |     
        -
    """
  ]

  return stages[retries_left]

main()