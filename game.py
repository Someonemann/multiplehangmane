#import all of the important suff (modules) that code would work properly
 from words import choose_word
from graphics import draw_hangman, display_word
# function for the guessing word
def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1
            print("Incorrect! You have {} attempts left.".format(attempts))
            draw_hangman(attempts)
        if set(word) <= set(guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nSorry, you ran out of tricks! The word is:", word)

if __name__ == "__main__":
    hangman()
