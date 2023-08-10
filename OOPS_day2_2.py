import OOPS_day2
print(OOPS_day2)

obj3 = OOPS_day2.person1("barca","camp nou", 1989)
print(obj3.yob1)
print(obj3._name1)
print(obj3._person1__surname1)
class person:
    _name = "prince"
    __surname = "francis"
    yob =1996

    def _age(self,current_year):
        return current_year-self.yob

    def __age1(self,current_year):
        return current_year-self.yob

obj = person()
print(obj)
print(obj._age(2023))
print(obj._person__age1(2023))
class employee(person):
    _name = "priya"
    __surname = "annies"
    yob = 1999

obj1 = employee()
print(obj1._age(2023))
print(obj1._person__age1(2023))
print(obj1)
print(obj1.yob)
print(obj1._name)
print(obj1._person__surname)
print(obj1._employee__surname)

