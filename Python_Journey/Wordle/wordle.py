import random
#from guesses import Guess


grid = [['-']*5 for i in range(5)] # prints out a grid that I plan to use for the words


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
        print(grid)
        for row in grid:
            print(' '.join(row))

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
                print("You need to try again")
          
        else:
            print("Length of Guess needs to be 5 letters long")
    if my_guess != correct_word:
        print("YIKES")
        


if __name__ == "__main__":
    main()