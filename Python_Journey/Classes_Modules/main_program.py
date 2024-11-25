# we will get user details and welcome them
#university, name, major
from students import Student



def get_student():
    name = input("Name: ")
    major = input("Major: ")
    uni = input("University: ")

    return Student(name, major, uni)

def main():
    my_student = get_student()
    my_student.university = "alabama"
    my_student.grades = [90,90,99,100]

    #greet the student
    print(f"Hello {my_student.name}. I hope you like going to {my_student.university} for {my_student.major}! Grade: {my_student.compute_letter_grade()}")

if __name__ == "__main__": # when you import programs into python it autimatically runs them - this prevents that from happening and says that it only runs when it is called directly from terminal
    main()