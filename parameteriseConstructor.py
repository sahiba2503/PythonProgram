
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Parameterized Constructor")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


obj = Student("Sahiba", 21)
obj.display()