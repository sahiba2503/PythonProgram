
class Student:

    DetailStore = []   # class variable (static)

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        print(self.name, self.roll)

    @staticmethod
    def addStudentDetail():
        print("function is called yes")

object1 = Student("sahiba", 2)

Student.DetailStore.append(object1)

Student.addStudentDetail()

print(Student.DetailStore)
