# a = 10
# b = 4

# try:
#     c = a /b 

# except:
#     print("b should not be zero")

# else:
#     print(c)        

"""Finally Block"""

# def fun(a):
#     try:
#         x = int(a)
#         return x
#     except Exception as e:
#         raise e
#     finally:
#          print("end of program")


# if __name__ == '__main__':
#     a = (input("Give numenator "))
#     # b = int(input("Give denominator "))
#     res = fun(a)

#     print(f"result is {res}")

"""User defined exception"""

class NegativeError(Exception):
    def __init__(self):
        self.msg = "-ve dimension" 

    def __str__(self):
        return self.msg    
       


def area(l,b):
    if l >= 0 and b >= 0 :
        a = l * b
        return a
    else:
        raise NegativeError()


if __name__ == '__main__':
    a = int(input("Give numenator "))
    b = int(input("Give denominator "))

    res = area(a,b)
    print(f"result is {res}")