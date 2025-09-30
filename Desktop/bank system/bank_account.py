class BankAccount:
    def __init__(self,name,accountNumber,balance = 0.00):
        self.__name = name
        self.__accountNumber = accountNumber
        self.__balance = balance
# make deposit
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

# make withdrawal  
    def withdraw(self,amount):
        if amount > self.__balance or amount <=0:
            return False
        else:
            self.__balance -= amount
            return True
# getter methods
    def get_name(self):
        return self.__name
    
    def get_account_number(self):
        return self.__accountNumber
# show balance
    def showBalance(self):
        return self.__balance
# setter methods
    def set_name(self, new_name):
        if new_name.strip():
            self.__name = new_name
            return True
        return False

    def set_account_number(self, new_account_number):
        if new_account_number.strip():
            self.__accountNumber = new_account_number
            return True
        return False
        

