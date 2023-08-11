class ineuron:

    students1= "data science "

    def students(self):
        print(self.students1)

i = ineuron()
i.students()
i.students1 = "data analytics"
i.students()

class ineuron1:

    __students1= "data science "

    def students(self):
        print(self.__students1)

    def student_change(self):   #setup function(set the value of variable via function)
        self.__students1=input()

i1 = ineuron1()
i1.students()
i1.__students1 = "big data"
i1.students()
i1.student_change()
i1.students()
