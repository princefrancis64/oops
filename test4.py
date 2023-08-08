class Person:
    def age(self,current_year,year_of_birth):
        return current_year-year_of_birth

    def email_id_input(self,email_id):
        print("take an email id from a peson and print it", email_id)

    def ask_name(self):
        name = input("tell me your name")
        return name

    def ask_dob(self):
        dob = input("tell me your date of birth")
        return dob

prince = Person()
priya = Person()
francis= Person()
annies = Person()

print(prince.age(2023,1996))
prince.email_id_input("prince.francis64@gmail.com")
prince.ask_name()
priya.ask_dob()

"""Task1 - in the past whatever questions i have given to you with respect to list,tuple,dict,set,string try to create separate
class for each and everything and restructure your code for all the segment and submit

instruction 1:always use exception handling
instruction 2:use logging as well

Reformat your code and submit it"""