import random
import string
#from guesses import Guess


grid = [['-']*5 for i in range(5)] # prints out a grid that I plan to use for the words
alphabet = string.ascii_lowercase
line_length = 6
alphabet_lines = []


def get_guess():
    guess = input("Guess:")
    #length = len(guess)

    return guess

def check_guess(real_guess,correct):
    if real_guess == correct:
        return True
    else:
        return False
    
def get_random_word():
        with open('data.txt', 'r') as f:
            data = f.read().splitlines()

        word_list = []
        word_list = [x.casefold() for x in word_list]

        for things in data:
            word_list.append(things) # putting all of the data into a list with commas seperating the words
        random_word = word_list[random.randint(0,3103)] # selects a random word

        return random_word

def check_letters(my_guess, correct): # this is not going to work with multiple letter words
    my_guess = set(my_guess)
    correct = set(correct)

    print(f'{my_guess.intersection(correct)} are in both words')

def correct_loc(my_guess, correct):
    for i in range(5):
        if my_guess[i] == correct[i]:
            print (f"{my_guess[i]} is in the correct spot ")

def print_alphabet():
    

    for i in range(0,len(alphabet), line_length):
        alphabet_lines.append(alphabet[i:i+line_length])

    return alphabet_lines

def print_grid_and_alphabet():
    alphabet_lines = print_alphabet()

    for i in range(5):
        grid_row  = ' '.join(grid[i])

        alphabet_row = alphabet_lines[i] if i < len(alphabet_lines) else ""
        print(f"{grid_row}    {''.join(alphabet_row)}")


  

def main():
    
    # for i in range(5):
    #     for j in range(5):
    #         print(grid[i][j], ' ',end = "")
    #     print()

    correct_word = get_random_word() # gets a random word and sets it as the correct word
    print(correct_word)
    my_guess = ""
    count = 0
    while my_guess != correct_word and count < 5 :
        #print(grid)
        print_grid_and_alphabet()
        # for row in grid:
        #     # this line prints the game grid
        #     print(' '.join(row), end= " ")
        #     # this line prints the alphabet 
        #     print_alphabet()
        #     print()

        my_guess = get_guess()

        if len(my_guess) == 5:
            if check_guess(my_guess,correct_word):
                grid[count] = list(my_guess)
                print("You got it!")
                for row in grid:
                    print(' '.join(row))
                break
            else:
                grid[count] = list(my_guess)
                count+=1 # this is needed to have the program only run 5 times - used in while loop
                check_letters(my_guess, correct_word)
                correct_loc(my_guess, correct_word)
                print("You need to try again")
          
        else:
            print("Length of Guess needs to be 5 letters long")
    if my_guess != correct_word:
        print("YIKES")
        


if __name__ == "__main__":
    main()