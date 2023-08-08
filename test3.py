class Person:

    def __init__(prince, name, surname, emailid, year_of_birth):
        prince.name1 = name
        prince.surname = surname
        prince.emailid = emailid
        prince.year_of_birth = year_of_birth

    def __init__(prince, name, surname):
        prince.name1 = name
        prince.surname = surname

    def age(prince, current_year):
        return current_year


prince_var = Person("Prince", "Francis")
francis_var = Person("Francis", "AL")
priya_var = Person("priya", "francis")
print(prince_var.name1 + prince_var.surname)
print(prince_var.name1)
print(francis_var.name1)
print(priya_var.name1)
print(type(prince_var))
print(prince_var.age(2023))
