
import logging
logging.basicConfig(filename="list.log",level=logging.INFO,format = '%(levelname)s %(name)s %(asctime)s %(message)s')

class lis:

    def rever(self,l):
        '''this is a function to reverse the list'''
        try:
            logging.info("this is the reversed list %s",l[::-1])
        except Exception as e:
            logging.exception("there is an error in the operation",e)


obj1 = lis()
obj1.rever([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}])


