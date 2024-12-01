class Letter_2:

    def __init__(self, letter):
        self.letter = letter
        self.color = "\033[0m"

    def set_color(self, color_code):
        self.color = color_code

    def get_letter(self):
        return self.letter
    
    def __str__(self):
        return f"{self.color}{self.letter}" # to add color to a string you put the color in front of the string itself and it applies when you
                                            # apply the __str__ method