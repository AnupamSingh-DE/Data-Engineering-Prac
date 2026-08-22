from datetime import datetime

class Profile:
    def __init__(self,fname,lname,year):
        self.__fname = fname
        self.__lname = lname 
        self.__year = year

    @property
    def name(self):
        return f'{self.__fname} {self.__lname}'

    @name.setter
    def name(self, name):
        names = name.strip().split()
        self.__fname = names[0]
        self.__lname = names[1]
    @property
    def age(self):
        current_year = datetime.now().year
        return current_year - self.__year
        


p1 = Profile('Anupam','Singh',2002)

print(p1.name)
print(p1.age)

