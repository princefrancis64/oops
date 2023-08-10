
from util.util1 import person2

obj = person2("real","madrid",1956)
print(obj.yob1)
class person1:

    def __init__(self,name,surname,yob):
        self._name1 = name
        self.__surname1 = surname
        self.yob1 = yob

prince = person1("prince","francis",1996)
print(prince._name1)
print(prince._person1__surname1)