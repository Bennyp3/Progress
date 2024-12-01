from letters_2 import Letter_2
import string 

alphabet = string.ascii_lowercase
alpha_objects = [Letter_2(i) for i in alphabet]
grid = [[' ']*6 for i in range(5)]
index = 0
for i in range(5):
    for j in range(6):
        if index < len(alpha_objects):
            grid[i][j] = str(alpha_objects[index])
            index +=1
#alpha_objects[3].set_color("\033[36m")

#x = [str(alpha_objects[3]),str(alpha_objects[5])]

#for i in x:
    #print(i)

#print(x) # if you print the list as a whole it calls the __repr__ method not the __str__ method 
          # the __str__ method is what is printing the objects in a human readable way

##row = ' '.join([str(alpha_objects[i]) for i in range(5)])  # First 5 letters
#print(row)
for row in grid:
    print(' '.join(row))


          