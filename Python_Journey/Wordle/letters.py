import string

    
class Letter:
   
    alphabet = string.ascii_lowercase
    line_length = 6
    alphabet_lines = []

    def __init__(self, letter):
        self.letter = letter
        self.color = "\033[0m"



    def set_color(self, color_code):
        self.color = color_code

    def __str__(self):
        return f"{self.color}{self.letter}\033[0m"
    
   