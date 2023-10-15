from User import User;
from Bank import Bank;
from Transaction import Transaction;
import random;

# Class Definition for Savings Account;
class SavingsAccount(User) :
    def __init__(self, name, email, address, balance = 0) -> None:
        super().__init__(name, email, address);
        self.__balance = balance;
        self.acc_no = f'SA-{random.randint(1, 1000)}';
        self.__trx_history = [];

    def deposit(self, amount):
        self.__balance += amount;
        Bank.setBalance(Bank.getBalance() + amount);
        print(f'Successfully Deposited Amount {amount}, in account {self.acc_no}, current balance is {self.__balance}');

    def withdraw(self, amount):
        if(amount > self.__balance) :
            print('Insufficient Funds');
            return;
        self.__balance -= amount;
        Bank.setBalance(Bank.getBalance() - amount);
        print(f'Withdrawn {amount} from account {self.acc_no}, current balance is {self.__balance}');
    
    def transfer(self, amount, acc_no) :
        if(self.__balance < amount) :
            print('Insufficient Balance.');
            return;
        transaction = Bank.transferAmount(self, amount, acc_no);
        if not transaction :
            print('Transactio Failed');
        else :
            self.__trx_history.append(transaction);


    @property
    def balance(self):
        return self.__balance;


    def issueLoan(self, amount) :
        if not Bank.loan :
            print('Loan is currently disabled');
            return;
        if(Bank.getBalance() <= 0) :
            print('Sorry! Bank is bankrupt');
            return;
        if(self.loan_count <= 0) :
            print(f'Sorry! You have already issued two loans and in {self.debt} debt to the bank');
            return;
        
        self.debt += amount;
        self.loan_count -= 1;
        Bank.issueLoan(amount);        
        print(f'You are issued a cash loan of {amount}. The amount is not added to your account');
        
    def viewTransactions(self) :
        print('Transactions are listed below.');
        for transaction in self.__trx_history :
            print(f'Transaction of {transaction.amount}, on {transaction.time} \n');

        if(self.__trx_history.__len__() == 0) :
            print('No transaction history');


#  Class Definition for Current Account;
class CurrentAccount(User) :
    def __init__(self, name, email, address, balance = 0) -> None:
        self.__balance = balance;
        self.acc_no = f'CA-{random.randint(1, 1000)}';
        self.__trx_history = [];
        super().__init__(name, email, address);

    def deposit(self, amount):
        self.__balance += amount;
        Bank.setBalance(Bank.getBalance() + amount);
        print(f'Successfully Deposited Amount {amount}, in account {self.acc_no}, current balance is {self.__balance}');

    def withdraw(self, amount):
        if(amount > self.__balance) :
            print('Insufficient Funds');
            return;
    
        self.__balance -= amount;
        Bank.setBalance(Bank.getBalance() - amount);
        print(f'Withdrawn {amount} from account {self.acc_no}, current balance is {self.__balance}');

    def transfer(self, amount, acc_no) :
        if(self.__balance < amount) :
            print('Insufficient Balance.');
            return;
        transaction = Bank.transferAmount(self, amount, acc_no);
        if not transaction :
            print('Transactio Failed');
        else :
            self.__trx_history.append(transaction);
            print('Transaction Completed');

    @property
    def balance(self):
        return self.__balance;

    def issueLoan(self, amount) :
        if not Bank.loan :
            print('Loan is currently disabled');
            return;
        if(Bank.getBalance() <= 0) :
            print('Sorry! Bank is bankrupt');
            return;
        if(self.loan_count <= 0) :
            print(f'Sorry! You have already issued two loans and in {self.debt} debt to the bank');
            return;
        
        self.debt += amount;
        self.loan_count -= 1;
        Bank.issueLoan(amount);        
        print(f'You are issued a cash loan of {amount}. The amount is not added to your account');


    def viewTransactions(self) :
        print('Transactions are listed below.');
        for transaction in self.__trx_history :
            print(f'Transaction of {transaction.amount}, on {transaction.time} \n');

        if(self.__trx_history.__len__() == 0) :
            print('No transaction history');