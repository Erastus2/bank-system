from bank_account import BankAccount

class Savings_Account(BankAccount):
    def __init__(self, name, accountNumber, balance =0 , interest_rate =0.05):
        super().__init__(name,accountNumber,balance)
        self.__interest_rate = interest_rate #private attribute
    
    def apply_interest(self):
        interest = self.showBalance() * self.__interest_rate
        self.deposit(interest)
        return interest
    def get_interest(self):
        return self.__interest_rate
    
    def set_interest_rate(self,newrate):
        if newrate >0:
            self.__interest_rate = newrate
            return True
        return False
    