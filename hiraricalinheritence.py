class A:
    def funA(self):
        print("This is A")

class B(A):
    def funB(self):
        print("This is B")

class C(A):
    def funC(self):
        print("This is C")

class D(A):
    def funD(self):
        print("This is D")

object = D()
object.funA()
object.funD()
