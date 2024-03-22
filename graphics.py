def draw_hangman(attempts):
    # Function to draw the hangman based on the number of attempts left
    pass  # Placeholder, actual implementation to be added

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()  # Strip removes any leading/trailing whitespace

