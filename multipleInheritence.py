class Father:
    def detailF(self):
        print("my father name is md arshad")

class Mother:
    def detailM(self):
        print("my mother name is raziya")

class Child(Father,Mother):
    def myInfor(self):
        print("my name is sahiba")

object = Child()
object.myInfor()
object.detailF()
object.detailM()
