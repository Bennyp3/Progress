from letters_2 import Letter_2
import string 
import random 

alphabet = string.ascii_lowercase
alpha_objects = [Letter_2(i) for i in alphabet] # creates a list of objects | Each object has a letter and a color associated

guess_grid = [["-"]*5 for _ in range(5)] # creates 5x5 grid for the guesses

alpha_grid = [[' ']*6 for _ in range(5)]


def altar_obj_colors(guess, correct):
    common_letters = set(guess).intersection(set(correct))
    for i in range(26):
        if alpha_objects[i].get_letter() in common_letters: # common_letters is a set of letters
            alpha_objects[i].set_color("\033[36m")

def create_alpha_grid(): # you need to altar the colors of the objects before you create the grid
    index = 0
    for row in range(5):
        for col in range(6):
            if index < len(alpha_objects):
                alpha_grid[row][col] = str(alpha_objects[index]) # you need to cast each individual object in the grid as a string
                index += 1

def get_guess():
    guess = input("Guess:").lower()
    return guess

def get_random_word():
        with open('data.txt', 'r') as f:
            data = f.read().splitlines() # reads data line by line

        word_list = []
        
        for things in data:
            word_list.append(things) # putting all of the data into a list with commas seperating the words
        random_word = word_list[random.randint(0,3103)] # selects a random word

        word_list = [x.casefold() for x in word_list]

        return random_word

def check_guess(real_guess,correct):
    if real_guess == correct:
        return True
    else:
        return False
    
def print_guess_grid():
     for row in guess_grid:
          print(' '.join(row))

def print_grids():
    count2 = 0
    for i in range(5):
        guess_grid_row = ' '.join(guess_grid[i])
        alpha_grid_row = ' '.join(alpha_grid[i])
        print(f"{guess_grid_row}    {alpha_grid_row}")



def main():
     my_guess = ""
     correct_word = get_random_word()
     count = 0
     print(correct_word)
     #alpha_objects[3].set_color("\033[36m")
     
     while my_guess != correct_word:
        altar_obj_colors(my_guess,correct_word)
        create_alpha_grid()
        #print_guess_grid()
        print_grids()
        my_guess = get_guess()
        if len(my_guess) == 5:
            if check_guess(my_guess, correct_word):
                guess_grid[count] = list(my_guess)
                print("CORRECT")
            else:
                guess_grid[count] = list(my_guess)
                count +=1
                print("please try again")

    
        else:
            print ("Your guess needs to be 5 letters long")

            
            


    
          






if __name__ == ("__main__"):
    main()