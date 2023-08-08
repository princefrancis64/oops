class Person:

    def __init__(self,name,surname,emailid,year_of_birth):
        self.name1 = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth


prince_var = Person("Prince" ,"Francis","prince.francis64@gmail.com",1996)
francis_var = Person("Francis" , "AL","francisal.fd@gmail.com", 1966)
priya_var=Person("priya","francis","priyafrancis62",1999)
print(prince_var.name1)
print(francis_var.name1)
print(priya_var.name1)
print(type(prince_var))
