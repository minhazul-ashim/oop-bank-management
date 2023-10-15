from User import User;
from Bank import Bank;
from Transaction import Transaction;

# Class Definition for Savings Account;
class SavingsAccount(User) :
    def __init__(self, name, email, address, balance = 0) -> None:
        self.__balance = balance;
        self.acc_no = f'SA-{Bank.saving_accounts.__len__() + 1}';
        super.__init__(name, email, address);

    def deposit(self, amount):
        self.__balance += amount;
        Bank.balance += amount;
        print(f'Successfully Deposited Amount {amount}, in account {self.acc_no}, current balance is {self.__balance}');

    def withdraw(self, amount):
        self.__balance -= amount;
        Bank.balance -= amount;
        print(f'Withdrawn {amount} from account {self.acc_no}, current balance is {self.__balance}');
    
    def transfer(self, amount, acc_no) :
        receiver = None;
        if(self.__balance < amount) :
            print('Insufficient Balance.');
            return;

        for account in Bank.saving_accounts :
            if(account.acc_no == acc_no) :
                receiver = account;

        for account in Bank.current_accounts :
            if(account.acc_no == acc_no) :
                receiver = account;

        if not receiver :
            print('Sorry! Account does not exist.');
        else :
            transaction = Transaction(self, amount, receiver);
            self.trx_history = transaction;
            Bank.trx_history = transaction;

    def checkBalance(self):
        print(f'The Savings Account, {self.acc_no} has balance of {self.__balance}');
        return self.__balance;

    def issueLoan(self, amount) :
        if not Bank.loan :
            print('Loan is currently disabled');
            return;
        if(Bank.balance <= 0) :
            print('Sorry! Bank is bankrupt');
            return;
        if(self.loan_count <= 0) :
            print(f'Sorry! You have already issued two loans and in {self.debt} debt to the bank');
            return;
        
        Bank.balance -= amount;
        self.debt += amount;
        self.loan_count -= 1;
        Bank.loan_issued += 1;
        



#  Class Definition for Current Account;
class CurrentAccount(User) :
    def __init__(self, name, email, address, balance) -> None:
        self.__balance = balance;
        self.acc_no = f'CA-{Bank.current_accounts.__len__() + 1}';
        super().__init__(name, email, address);

    def deposit(self, amount):
        self.__balance += amount;
        Bank.balance += amount;
        print(f'Successfully Deposited Amount {amount}, in account {self.acc_no}, current balance is {self.__balance}');

    def withdraw(self, amount):
        self.__balance -= amount;
        Bank.balance -= amount;
        print(f'Withdrawn {amount} from account {self.acc_no}, current balance is {self.__balance}');

    def transfer(self, amount, acc_no) :
        receiver = None;
        if(self.__balance < amount) :
            print('Insufficient Balance.');
            return;

        for account in Bank.saving_accounts :
            if(account.acc_no == acc_no) :
                receiver = account;

        for account in Bank.current_accounts :
            if(account.acc_no == acc_no) :
                receiver = account;

        if not receiver :
            print('Sorry! Account does not exist.');
        else :
            transaction = Transaction(self, amount, receiver);
            self.trx_history = transaction;
            Bank.trx_history = transaction;

    def checkBalance(self):
        print(f'The Current Account, {self.acc_no} has balance of {self.__balance}');
        return self.__balance;

    def issueLoan(self, amount) :
        if not Bank.loan :
            print('Loan is currently disabled');
            return;
        if(Bank.balance <= 0) :
            print('Sorry! Bank is bankrupt');
            return;
        if(self.loan_count <= 0) :
            print(f'Sorry! You have already issued two loans and in {self.debt} debt to the bank');
            return;
        
        Bank.balance -= amount;
        self.debt += amount;
        self.loan_count -= 1;
        Bank.loan_issued += 1;