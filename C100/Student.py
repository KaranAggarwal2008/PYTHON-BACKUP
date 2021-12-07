class Student(object):
    def __init__(self, nameInput, ageInput, genderInput, levelInput, gradesInput):
        self.name = nameInput
        self.age = ageInput
        self.gender = genderInput
        self.level = levelInput
        self.grades = gradesInput

    def study(self):
        print("STUDYING")

    def increase_grade(self):
        self.grades = +1
        print("The stude")

    def setGrade(self, courseInput, gradesInput):
        self.grades[courseInput] = gradesInput

    def getGrade(self, courseInput):
        return self.grades[courseInput]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)
    
    
#Define some students 
john = Student("John", 12, "male", 6, {"math": 3.3}) 
jane = Student("Jane", 12, "female", 6, {"math": 3.5})

# Now we can get to the grades easily
print(john.getGPA())
print(jane.getGPA())

===========================================================================================================

        """class Student(object):
    name = ""
    age = 0
    major = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

def make_student(name, age, major):
    student = Student(name, age, major)
    return student
        """


