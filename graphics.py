def draw_hangman(attempts):
    # Function to draw the hangman based on the number  left
    pass  # Placeholder, actual implementation to be added
# function to display words, and things with guesse_letters variable
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " " #will add letter, if it the guess is right
        else:
            displayed_word += "_ "
    return displayed_word.strip()  # Strip will clean any leading/trailing whitespace

