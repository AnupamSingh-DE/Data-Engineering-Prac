# a = int(input("Give numenator "))
# b = int(input("Give denominator "))
# print(f"a = {a} and b = {b}")


# try:
#     c = a / b
#     print(c)
# except:
#     print("denominator should not be zero")


# l1 = [1,2,3,4,5,6]
# ind = int(input("enter index "))
# try:
#     print(f"Index element is {l1[ind]}")
# except:
#     print("Enter valid index")

# print("End of Program")

"""exception handling is required when we are using function for this kind of simple program we can handle exception using conditons like if else"""

def div(a,b):
    if b != 0:
        c = a // b 
        return c
    else:
        raise ZeroDivisionError



if __name__=='__main__':
    a = int(input("Give numenator "))
    b = int(input("Give denominator "))
    try:
        res = div(a,b)
        print(f"Result is {res}")
    except:
        print("ZeroDivisionError")    

