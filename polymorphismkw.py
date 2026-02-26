class studentInformation:
    def student_info(self,**kwargs):
        for key,value in kwargs.items():
            print(key,":",value)
object = studentInformation()
object.student_info(name="sahiba",age=21, course="BCA")
object.student_info(name="sahiba2",age=21, course="BCA")
object.student_info(name="sahiba3",age=21, course="BCA")
object.student_info(name="sahiba4",age=21, course="BCA")
object.student_info(name="sahiba5",age=21, course="BCA")