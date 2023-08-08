import logging
logging.basicConfig(filename="string_tasks.log",level=logging.INFO,format = '%(levelname)s %(name)s %(asctime)s %(message)s')

class string_tasks:
    def extract(self,s):
        '''this is a program to extract data from index one to index 300 with a jump of 3 '''
        try:
            logging.info("this is the result %s",s[1:300:3])
        except:
            logging.info("there is somthing wrong with the code")

    def splitandupper(self,s):
        '''split a string after conversion of entire string in uppercase'''
        try:
            logging.info("this is the result-%s",s.upper().split())
        except:
            logging.info("there is somthing wrong with the code")

    def lower(self,s):
        '''to convert the whole string into lower case '''
        try:
            logging.info("this is the result-%s",s.lower())
        except:
            logging.info("there is somthing wrong with the code")


    def capitalize(self,s):
        '''Try to capitalize the whole string '''
        try:
            logging.info("this is the result-%s",s.capitalize())
        except:
            logging.info("there is somthing wrong with the code")


    def replace(self,s):
        '''Replace a string charecter by another charector'''
        try:
            logging.info("this is the result-%s",s.replace("P", "p"))
        except:
            logging.info("there is somthing wrong with the code")





obj1 = string_tasks()
obj1.extract("this is My First Python programming class and i am learNING python string and its function")
obj1.splitandupper("this is My First Python programming class and i am learNING python string and its function")
obj1.lower("this is My First Python programming class and i am learNING python string and its function")
obj1.capitalize("this is My First Python programming class and i am learNING python string and its function")
obj1.replace("Prince")