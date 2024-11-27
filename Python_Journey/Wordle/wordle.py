import random

with open('data.txt', 'r') as f:
    data = f.read().splitlines()

word_list = []

for things in data:
    word_list.append(things) # putting all of the data into a list with commas seperating the words

random_word = word_list[random.randint(0,3103)] # selects a random word
#print(random_word) 

# grid = [['-']*5 for i in range(5)] # prints out a grid that I plan to use for the words

# for i in range(5):
#     for j in range(5):
#         print(grid[i][j], ' ',end = "")
