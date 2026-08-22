# # How to define a class its variables(fields) and methods and how to use them in object

# class Rectangle:
#     def __init__(self):   # Constructor. we are using self because self is a reference to the current object
#         self.length = 10
#         self.breadth = 5

#     def area(self):  # Method
#         return self.length * self.breadth

#     def perimeter(self):
#         return 2*(self.length + self.breadth)

# r = Rectangle() # --> object == instance


# print("Length:",r.length)
# print("Breadth:",r.breadth)
# print("Area:",r.area())
# print("Perimeter:",r.perimeter())


#--------------------------------------------------------------------------------------------------------------------------------------------------------------

## Self and constructor

# class Rectangle:
#     def __init__(self,length,breadth):
#         print("self id",id(self))
#         self.length = length.  # instance variables
#         self.breadth = breadth

#     def area(self):
#         return self.breadth*self.length

#     def perimeter(self):
#         return 2*(self.breadth + self.length)


# r = Rectangle(10,20)
# print("r id",id(r))
# print("Length:",r.length)
# print("Breadth:",r.breadth)
# print("Area:",r.area())
# print("Perimeter:",r.perimeter())   
# print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
# r1 = Rectangle(123,2320)
# print("r1 id",id(r1))
# print("Length:",r1.length)
# print("Breadth:",r1.breadth)
# print("Area:",r1.area())
# print("Perimeter:",r1.perimeter())  

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

#Instance variable and methods
# objcets are also called as instance
# we can create a instance variable upon an object also


# class Test:
    
#     def __init__(self):
#         self.a = 10

#     def fun(self):
#         self.b = 4


#     def show(self):
#         print(self.a)    
#         print(self.b)
#         print(self.c)

# w = Test()

# w.fun()
# w.c = 40
# w.show()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
""" Class variables and methods
 class variables are accessed using class name inside instance method
 class variable are used for shared data for all the instances of a class they will have 
    only one copy, only one and that is there for all. 
    Instance is able to give class information also """


# class Rectangle:
#     count = 0 
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#         Rectangle.count += 1

#     def area(self):
#         return self.length*self.breadth

#     def perimeter(self):
#         return 2*(self.length+self.breadth)

#     @classmethod
#     def get_count(cls):
#         return cls.count


# r = Rectangle(10,23)
# r2 = Rectangle(11,23)
# print(Rectangle.get_count())
# print(r.area())


#--------------------------------------------------------------------------------------------------------------------------------------------------------------
""" Static Methods """


# class Rectangle:
#     def __init__(self,l,b):
#         self.length = l
#         self.breadth = b

#     def area(self):
#         return self.length * self.breadth    
    
#     def parimeter(self):
#         return 2*(self.length + self.breadth)
#     # @staticmethod
#     def calc_area(length,breadth):
#         return length*breadth
    

# r = Rectangle(23,4)
# print("Calling calc", Rectangle.calc_area(10,3))

# print(r.calc_area(10,32))    



#--------------------------------------------------------------------------------------------------------------------------------------------------------------
"""Property methods""" 

class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
        
    @property
    def length(self):
        return self._length  
    
    @property
    def breadth(self):
        return self._breadth        
    @length.setter
    def length(self,leng):

        if leng >= 0:
             self._length = leng
        else:
            self._length = 1  

    @breadth.setter
    def breadth(self,bred):
        if bred >= 0:
            self._breadth = bred
        else:
            self._breadth = 1    


r = Rectangle(10,12)

r.length = 2-3
print(r.length)
  

        