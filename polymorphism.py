#polymorphism
class AddSomeNumber:
    def sum(self, *numbers):
        print("Sum of numbers is:", sum(numbers))
    
obj = AddSomeNumber()

obj.sum(5, 9)
obj.sum(5, 9, 3)
obj.sum(5, 9, 3, 2)