import logging
logging.basicConfig(filename = "Tasks_May28.log",level = logging.DEBUG,format = "%(levelname)s %(name)s %(asctime)s %(message)s")

class Tasks_May28:

    def extract_list(self,l):
        '''Try to extract all the list entity '''
        try:
            l1= []
            for i in l:
                if type(i) == list:
                    l1.append(i)
                    logging.info("all the list entities would be %s",l1)
            return l1
        except Exception as e:
            logging.error(e)

    def extract_dict(self,l):
        '''Try to extract all the dictionary entity '''
        try:
            l1= []
            for i in l:
                if type(i) == dict:
                    l1.append(i)
                    logging.info("all the dictionary entities would be %s",l1)
            return l1
        except Exception as e:
            logging.error(e)


    def extract_tuple(self,l):
        '''Try to extract all the tuple entity '''
        try:
            l1= []
            for i in l:
                if type(i) == tuple:
                    l1.append(i)
                    logging.info("all the tuple entities would be %s",l1)
            return l1
        except Exception as e:
            logging.error(e)


    def extract_num(self,l):
        '''Try to extract all the numerical data it may b a part of dict key and values '''
        try:
            l1 = []
            for i in l:
                if type(i) == tuple or type(i) == set or type(i) == list:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                elif type(i) == dict:
                    for j in i.items():
                        for k in j:
                            if type(k) == int:
                                l1.append(k)
            logging.info("all the numerical values would include %s",l1)
            return l1
        except Exception as e:
            logging.error(e)

    def sum_num(self,l1):
        '''Try to give summation of all the numeric data '''
        try:
            sum= 0
            for i in l1:
                sum = sum + i
            logging.info("the sum of all the numerical data in the list is %s",sum)
            return sum

        except Exception as e:
            logging.error(e)

    def odd(self,l1):
        '''Try to filter out all the odd values out all numeric data which is a part of a list '''
        l=[]
        try:
            for i in l1:
                if i % 2 != 0:
                    l.append(i)
            logging.info("The list including all the odd values would be %s", l)
            return l

        except Exception as e:
            logging.error(e)

    def extract_ineuron(self,l):
        '''Try to extract "ineruon" out of this data'''
        try:
            for i in l:
                if type(i) == dict:
                    for j in i.items():
                        for k in j:
                            if k == 'ineuron':
                                logging.info(k)
        except Exception as e:
            logging.error(e)

    def num_occurences(self,l):
        '''Try to find out a number of occurrences of all the data '''
        try:
            l1 = []
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        l1.append(j)
                elif type(i) == dict:
                    for j in i.items():
                        for k in j:
                            l1.append(k)
            l2 = set(l1)
            for i in l2:
                logging.info("%s is included in the list %s number of times",i, l1.count(i))
        except Exception as e:
            logging.error(e)

    def keys(self,l):
        '''Try to find out number of keys in dict element'''
        try:
            l2 = []
            for i in l:
                if type(i) == dict:
                    for k in i:
                        l2.append(k)
            logging.info(len(l2))
        except Exception as e:
            logging.error(e)

    def string_data(self,l):
        '''Try to filter out all the string data'''
        try:
            l3 = []
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            l3.append(j)
                else:
                    for j in i.items():
                        for k in j:
                            if type(k) == str:
                                l3.append(k)
            logging.info("Here is the list of all the string data present in the list %s",l3)
            return l3
        except Exception as e:
            logging.error(e)


    def alpha_num(self,l):
        '''Try to Find  out alphanum in data'''
        try:
            l3 = []
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            if j.isdigit() == False and j.isalpha() == False and j.isalnum() == True:
                                l3.append(j)
                else:
                    for j in i.items():
                        for k in j:
                            if type(k) == str:
                                if k.isdigit() == False and k.isalpha() == False and k.isalnum() == True:
                                    l3.append(k)
            logging.info("Here is the list including all the alphanumerical entities in the list %s",l3)
            return l3
        except Exception as e:
            logging.error(e)

    def mutli(self,l1):
        '''Try to find out multiplication of all numeric value in  the individual collection inside dataset'''
        try:
            multi = 1
            for i in l1:
                multi = multi * i
            logging.info(multi)
        except Exception as e:
            logging.error(e)


    def unwrap(self,l):
        '''Try to unwrap all the collection inside collection and create a flat list '''
        try:
            l4 = []
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        l4.append(j)
                else:
                    for j in i.items():
                        for k in j:
                            l4.append(k)
            logging.info(l4)
        except Exception as e:
            logging.error(e)


obj1 = Tasks_May28()
obj1.extract_list([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj1.extract_dict([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj1.extract_tuple([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj1.extract_num([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj1.sum_num([1, 2, 3, 4, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 45, 4, 5, 23, 3, 6, 7, 8])
obj1.odd([1, 2, 3, 4, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 45, 4, 5, 23, 3, 6, 7, 8])
obj1.extract_ineuron([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj1.num_occurences([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj1.keys([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj1.string_data([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj1.alpha_num([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])
obj1.mutli([1, 2, 3, 4, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 45, 4, 5, 23, 3, 6, 7, 8])
obj1.unwrap([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]])

