

class paisaNhiHaiBro(Exception):
    pass


class BankAccount():

    acc_counter = 1000

    def __init__(self,name, balance = 0):
        BankAccount.acc_counter += 1
        self.name = name 
        self.__accNo = self.acc_counter
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount positive hona chahiye!")
        self.__balance += amount
        return self.__balance

    def withdrawl(self,amount):
        if self.__balance > 0 and self.__balance > amount:
            self.__balance = self.__balance - amount
            return self.__balance
        else:
            raise paisaNhiHaiBro ("Insufficient Funds")

    def getBanlace(self):
        return self.__balance

    def __str__(self):
        return (f"Account No : {self.__accNo} |"
                f"Account Holder Name : {self.name} |"
                f"Remaninig Balance : {self.__balance}")


c1 = BankAccount("Anupam",456789)
print(c1)
print(c1.withdrawl(5354343300))
print(c1.getBanlace())