from bank_account import BankAccount
from savings_account import Savings_Account

def main():
    #creating account
    account = Savings_Account("Erastus ", '10247010005',500,0.05) 
    while True:
        print("******Savings Account menu******")
        print("1 :View Account Information")
        print("2 :Deposit money")
        print("3 :Make withdrawal")
        print("4 :show balance")
        print("5 :Apply interest")
        print("6 :update Account name")
        print("7 :update Account number")
        print("8 :Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            print("$$$$ Account information$$$$")
            print(f"Name : {account.get_name()}")
            print(f"Account number :{account.get_account_number()}")
            print(f"Interest rate: {account.get_interest()* 100}%")
            print(f"Current balance :{account.showBalance()}")

        elif choice == "2":
            amount = float(input("Enter deposit account :"))
            if account.deposit(amount):
                print("Deposit successfull.")
            else:
                print("The amount must be positive")
        elif choice =="3":
            amount = float(input("Enter amount to withdraw :"))
            if account.withdraw(amount):
                print("You have successfully withdraw")
            else:
                print("Invalid or Insufficient")
        elif choice == "4":
            print(f"current balance :{account.showBalance()}")
        elif choice =="5":
            interest = account.apply_interest()
            print(f"Interest of {interest:.2f} applied  new balance {account.showBalance()}")
        elif choice == "6":
            newName = input("Update your name:")
            if account.set_name(newName):
                print("Name updated successfully")
            else:
                print("Enter a valid name")
        elif choice == "7":
            new_account_number = input("Update your account number:")
            if account.set_account_number(new_account_number):
                print("Account number updated successfully")
            else:
                print("Enter a valid account number")
        elif choice == "8":
            print("Thank you for banking with us")
            break
        else:
            print("Invalid choice, Please try again!!")


if __name__ == "__main__":
    main()