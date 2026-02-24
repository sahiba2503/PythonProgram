class gradParent:
    def detailG(self):
         print("my dear grand paa")

class parent(gradParent):
    def detailP(self):
         print("and my papa")

class child(parent):
    def detailmy(self):
         print("i am fine")

object = child()
object.detailmy()
object.detailG()
object.detailP()
