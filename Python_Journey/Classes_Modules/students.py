class Student:
    validUniversities = ['UGA','MIT','HARVARD','UCLA']
    validUniversities = [x.casefold() for x in validUniversities]

    def __init__ (self, name, major, university, grades = []):
        self.name = name
        self.major = major
        self.university = university
        self.grades = grades.copy()
        #casefold converts to lowercase
        
        
    def compute_letter_grade(self):
        # if list is empty
        if not self.grades:
            return 'F'
        else:
            avg = sum(self.grades)/len(self.grades)
            if avg >=90:
                return 'A'
            elif avg >= 80:
                return 'B'
            elif avg>= 70:
                return 'C'
            elif avg >= 60:
                return 'D'
            else:
                return 'F'



    #getter
    @property
    def university(self):
        return self._university

    #setter
    @university.setter
    def university(self, value):
            # casefold converts to lowercase
            if value.casefold() in Student.validUniversities:
                self._univeristy = value.upper() # save it as uppercase
            else:
                raise ValueError("Invalid University")
            self._university = value

    def __str__(self):
        return f"{self.name}, {self.major}, {self.university}, {self.compute_letter_grade()}"