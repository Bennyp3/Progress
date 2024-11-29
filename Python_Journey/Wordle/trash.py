import random
import string
from letters import Letter  # Import the Letter class

grid = [['-']*5 for _ in range(5)]  # 5x5 grid for the game
alphabet = string.ascii_lowercase
alphabet_letters = [Letter(i) for i in alphabet]
line_length = 6
alphabet_lines = []  # Store the alphabet in lines

def get_guess():
    """Get a guess from the player."""
    return input("Guess:").lower()

def check_guess(real_guess, correct):
    """Check if the guess is correct."""
    return real_guess == correct

def get_random_word():
    """Get a random word from the word list."""
    with open('data.txt', 'r') as f:
        data = f.read().splitlines()

    word_list = [x.casefold() for x in data]  # Ensure all words are lowercase
    random_word = random.choice(word_list)  # Select a random word
    return random_word

def check_letters(my_guess, correct):
    """Check which letters in the guess are correct (intersection)."""
    my_guess = set(my_guess)
    correct = set(correct)
    print(f'{my_guess.intersection(correct)} are in both words')

def correct_loc(my_guess, correct):
    """Check if the letters are in the correct position."""
    for i in range(5):
        if my_guess[i] == correct[i]:
            print(f"{my_guess[i]} is in the correct spot")

def print_alphabet():
    """Generate the alphabet in rows, and return it."""
    alphabet_lines = [alphabet[i:i+line_length] for i in range(0, len(alphabet), line_length)]
    return alphabet_lines

def print_grid_and_alphabet():
    """Print the grid and the alphabet, with colors."""
    alphabet_lines = print_alphabet()
    for i in range(5):
        grid_row = ' '.join(grid[i])  # Join grid row with spaces
        # Print corresponding row of alphabet with colors
        alphabet_row = ''.join([str(letter) for letter in alphabet_letters[i*line_length:(i+1)*line_length]])
        print(f"{grid_row}    {alphabet_row}")

def change_colors_of_alphabet(guess, correct_word):
    """Change colors of alphabet letters based on the guess."""
    common_letters = set(guess).intersection(set(correct_word))

    for letter in alphabet_letters:
        if letter.letter in common_letters:
            letter.set_color("\033[92m")  # Set color to green for matching letters
        else:
            letter.set_color("\033[0m")  # Reset to default color for others

def main():
    correct_word = get_random_word()  # Get a random word from the list
    print(correct_word)  # Print the correct word for debugging
    my_guess = ""
    count = 0

    while my_guess != correct_word and count < 5:
        print_grid_and_alphabet()  # Print the grid and alphabet

        my_guess = get_guess()  # Get the user's guess

        if len(my_guess) == 5:
            if check_guess(my_guess, correct_word):
                grid[count] = list(my_guess)
                print("You got it!")
                for row in grid:
                    print(' '.join(row))  # Print the final grid
                break
            else:
                grid[count] = list(my_guess)
                change_colors_of_alphabet(my_guess, correct_word)  # Change colors based on the guess
                count += 1  # Increment the guess count
                check_letters(my_guess, correct_word)
                correct_loc(my_guess, correct_word)
                print("You need to try again.")
        else:
            print("Length of Guess needs to be 5 letters long")

    if my_guess != correct_word:
        print("YIKES")

if __name__ == "__main__":
    main()
