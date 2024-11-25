# we will get user details and welcome them
#university, name, major
from students import Student
from logger import Logger
import random

def get_student():
    name = input("Name: ")
    major = input("Major: ")
    uni = input("University: ")

    return Student(name, major, uni)

def main():
    # create a logger object 
    my_logger = Logger('students.txt')

    for _ in range(3):
        my_student = get_student()
        # my_student.university = "alabama"
        my_student.grades = [random.uniform(0,100) for _ in range(5)] # generates 5 random grades
        my_logger.logRow(str(my_student))

    #greet the student
    #print(f"Hello {my_student.name}. I hope you like going to {my_student.university} for {my_student.major}! Grade: {my_student.compute_letter_grade()}")

if __name__ == "__main__": # when you import programs into python it autimatically runs them - this prevents that from happening and says that it only runs when it is called directly from terminal
    main()