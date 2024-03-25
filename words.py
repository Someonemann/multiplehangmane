# we have list with the some words, and module random, that will generate random woords from our list
import random
def choose_word():
    words = ["python", "hangman", "programming", "computer", "game", "developer", "coding"]
    return random.choice(words)
