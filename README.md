Bank System (OOP in Python)

This is a simple Bank Management System built using Object-Oriented Programming (OOP) concepts in Python.
It demonstrates encapsulation, inheritance, and polymorphism through classes for managing bank accounts and savings accounts.

 Features

Create a Savings Account with:

Name

Account Number

Initial Balance

Interest Rate

Deposit money

Withdraw money with validation (no overdraft, positive amount only)

Check account balance

Apply interest to balance

Update account holder’s name and account number

Menu-driven console interface

📂 Project Structure
bank-system/
│── bank_account.py       # Base class: BankAccount
│── savings_account.py    # Derived class: Savings_Account (inherits BankAccount)
│── main.py               # Main program (menu interface)
│── README.md             # Project documentation

How to Run

Clone the repository:

git clone https://github.com/your-username/bank-system.git
cd bank-system


Run the program:

python main.py


Follow the on-screen menu to interact with your account.

Example Usage
******Savings Account menu******
1 :View Account Information
2 :Deposit money
3 :Make withdrawal
4 :Show balance
5 :Apply interest
6 :Update Account name
7 :Update Account number
8 :Exit

 Concepts Demonstrated

Encapsulation → Private attributes for account details.

Inheritance → Savings_Account inherits from BankAccount.
