import string

bet = []
letters = string.ascii_lowercase


line_length = 6
for i in range(0, len(letters), line_length):
    print(letters[i:i + line_length])



