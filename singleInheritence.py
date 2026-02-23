class Parent:
    def greet(self):
        print("hellow sahiba")

class Child(Parent):
    def display(self):
        print("this is child class")
object = Child()
object.greet()
object.display()

