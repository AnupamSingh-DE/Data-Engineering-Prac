
class insufficientBalance(Exception):
    pass


class BankAccount:
    acc_counter = 100
    
    def __init__(self,name,balance = 0):
        self.name = name
        BankAccount.acc_counter += 1
        self.__acc = BankAccount.acc_counter 
        self.__balance = balance

    def deposite(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if 0 < self.__balance and amount < self.__balance:
            self.__balance -= amount
            return (self.__balance)
        else: 
            raise  insufficientBalance("not enough funds")   

    def getBalance(self):
        return self.__balance

    def details(self):
        return self.name , self.__acc, self.__balance
    
anupam = BankAccount("Anupam", 100)

print(anupam.getBalance())
print(anupam.withdraw(10))
print(anupam.details())