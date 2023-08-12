# 1st file
class Person:
    def __init__(self,name,surname,emailid,year_of_birth):
        self.name = name
        self.surname= surname
        self.emailid=  emailid
        self.year_of_birth  = year_of_birth


prince_var = Person("Prince","francis", "princefrancis03",1996)
# print(prince_var.name)
# print(prince_var.surname)
# print(prince_var.emailid)
# print(prince_var.year_of_birth)

# ----------------------------------------------------------------------------------------------------------
# 2nd file

class Person:

    def __init__(prince,name,surname,emailid,year_of_birth):
        prince.name = name
        prince.surname = surname
        prince.emailid = emailid
        prince.year_of_birth = year_of_birth


    def current_age(self,current_year):
        return current_year-self.year_of_birth

prince_var = Person("prince","francis", "prince.francis64", 1996)
# print(prince_var.current_age(2023))

# ------------------------------------------------------------------------------------------------------
#3rd file
class Person:

    def __init__(self, name, surname, emailid, year_of_birth):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth

    def __init__(self, name, surname):
        self.name= name
        self.surname = surname


prince_var = Person("prince","francis")
# print(prince_var.name)

# --------------------------------------------------------------------------------------------------------------
# 4th file
class Person:
    def age(self,current_year,year_of_birth):
        return current_year - year_of_birth

    def email_id(self,emailid):
        print("the email id entered is ",emailid)
    def ask_name(self):
        name= input()
        return name
    def ask_dob(self):
        doy = int(input())
        print("the date of year entered is", doy)

prince_var = Person()
# print(prince_var.age(2023,1996))
# prince_var.email_id("prince.francis64@gmail.com")
# print(prince_var.ask_name())
# prince_var.ask_dob()

# ---------------------------------------------------------------------------------------------------
# 5th file
class person1:

    def __init__(self,name,surname,yob):
        self._name = name
        self.__surname = surname
        self.yob = yob

prince = person1("prince","francis",1996)
#print(prince._name)
# print(prince._person1__surname)

# --------------------------------------------------------------------------------------------------
# 6th file
class person:
    _name = "prince"
    __surname = "francis"
    yob = 1996

    def _age(self,current_year):
        return current_year - self.yob

    def __age1(self,current_year):
        return current_year - self.yob

obj = person()
# print(obj._age(2023))
# print(obj._person__age1(2023))


class employee(person):
    _name = "priya"
    __surname = "annies"
    yob = 1999

obj1 = employee()
# print(obj1._age(2023))
# print(obj1._person__age1(2023))
# print(obj1._employee__surname)
# print(obj1._person__surname)

# --------------------------------------------------------------------------------------------------
# 7th file
class car:
    def __init__(self,body,engine,tyre):
        self.body = body
        self.engine =engine
        self.tyre = tyre

    def mileage(self):
        print("mileage of the car is less than bike")
c =car("solid","Petrol" ,"radial")
# print(c)

class tata(car):
    pass

t = tata("ALPHA" ,"1.2 Petrol","16 inch alloy")
# print(t.body)
# t.mileage()
# print(t.engine)
# print(t.tyre)

# ------------------------------------------------------------------------------
# 8th file

class bank:
    def transaction(self):
        print("total transaction value")

    def account_opening(self):
        print("this will show if the account is opened or not")

    def deposit(self):
        print("this will show the deposited amount")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show all the transactions happened to icici through hdfc bank")

class icici(HDFC_bank):
    pass

i = icici()
# i.deposit()
# i.hdfc_to_icici()
# i.transaction()
# i.account_opening()

# ---------------------------------------------------------------------
# 9th file
class bank:
    def transaction(self):
        print("total transaction value")

    def account_opening(self):
        print("this will show if the account is opened or not")

    def deposit(self):
        print("this will show the deposited amount")

    def test(self):
        print("this is test method from bank class")

class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show all the transactions happened to icici through hdfc bank")

    def test(self):
        print("this is test method from HDFC_bank class")

class ineuron_bank:
    def ineuron_to_icici(self):
        print("print an account status to icici")

class icici(HDFC_bank,bank,ineuron_bank):
    pass

i = icici()
# i.test()

# ------------------------------------------------------------------------------------
# 10th file

class ineuron:
    def student(self):
        print("print the details of the students")

    def acheivers(self):
        print("print the list of all acheivers")

    def hall_of_fame(self):
        print("check everyone from the hall of fame list")


class ineuron_vision(ineuron):
     def student(self):   #method overriding
        print("these are filtered student list")

iv = ineuron_vision()
# iv.student()

# ----------------------------------------------------------------------------------------
# 11th file
# abstraction
class ineuron:
    __students = "data science"


    def students(self):
        print("print the class of students" , ineuron.__students)

i  = ineuron()
# i.students()

# --------------------------------------------------------------------------------------------
# 12th file
# encapsulation

class ineuron:
    students1 = "data science"

    def students(self):
        print(self.students1)

i  = ineuron()
# i.students()
i.students1 = "data analytics" #we can change the class variable by using the object
# i.students()

class ineuron1:
    __students1 = "data science"

    def students(self):
        print(self._ineuron1__students1)

    def students_change(self):
        self.__students1 = "big data"

i1 = ineuron1()
# i1.students()
# i1.__students1 = "big data"
# i1.students()
# i1.students_change()
# i1.students()
# -------------------------------------------------------------------------------------------------------
# 13th file
# polymorphism

class ineuron:

    def students(self):
        print("print a students details")


class class_type:

    def students(self):
        print("print the class type of students")

def external(a):
    a.students()

i = ineuron()
j = class_type()

external(i)
external(j)


