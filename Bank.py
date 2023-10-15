from Transaction import Transaction;

class Bank :
    __saving_accounts = [];
    __current_accounts = [];
    __balance = 0;
    loan = False;
    __trx_history = [];
    __loan_issued = 0;
    __loan_amount = 0;

    @classmethod
    def checkLoanAmount(cls) :
        print(f'Total amount of loan {cls.__loan_amount} and total loans issued {cls.__loan_issued}');

    @classmethod
    def toggleLoan(cls) :
        if cls.loan :
            print('Loan turned off');
            cls.loan = False;
        else :
            print('Loan turned on');
            cls.loan = True;

    @classmethod
    def createAccount(cls, account, op) :
        # if op == 1 then savings account, if op == 2 then current account;
        if(op == 1) :
            cls.__saving_accounts.append(account);
            return account;
        elif(op == 2) :
            cls.__current_accounts.append(account);
            return account;
        else :
            print('Invalid Option');
            return None;
        
    @classmethod
    def removeAccount(cls, acc_no) :
        for account in cls.__saving_accounts :
            if(account.acc_no == acc_no) :
                cls.__saving_accounts.remove(account);
                print('Account removed');
                return;
        for account in cls.__current_accounts :
            if(account.acc_no == acc_no) :
                cls.__current_accounts.remove(account);
                print('Account removed');
                return;
        print('No account found with that id');

    @classmethod
    def getBalance(cls) :
        return cls.__balance;

    @classmethod
    def setBalance(cls, val) :
        cls.__balance = val;

    @classmethod
    def viewAccountList(cls) :
        print('The savings accounts are below');
        for account in cls.__saving_accounts :
            print(f'Account Holder {account.name} and AC/NO: {account.acc_no}\n');
    
        print('The current accounts are below');
        for account in cls.__current_accounts :
            print(f'Account Holder {account.name} and AC/NO: {account.acc_no}\n');

    @classmethod
    def viewTransactins(cls) :
        print('Transactions are listed below.');
        for transaction in cls.__trx_history :
            print(f'Transaction of {transaction.amount}, on {transaction.time} \n');

    @classmethod
    def authorizeUser(cls, acc_no) :
        for account in cls.__saving_accounts :
            if(account.acc_no == acc_no) :
                return account;
        for account in cls.__current_accounts :
            if(account.acc_no == acc_no) :
                return account;

        return None;

    @classmethod
    def addTransaction(cls, trx) :
        cls.__trx_history.append(trx);

    @classmethod
    def issueLoan(cls, amount) :
        cls.__loan_issued+=1;
        cls.__loan_amount += amount;
        cls.__balance -= amount;
        print('Loan issued successfully.');

    @classmethod
    def transferAmount(cls, sender, amount, acc_no) :
        receiver = None;

        for account in cls.__saving_accounts :
            if(account.acc_no == acc_no) :
                receiver = account;

        for account in cls.__current_accounts :
            if(account.acc_no == acc_no) :
                receiver = account;

        if not receiver :
            print('Sorry! Account does not exist.');
            return None;
        else :
            transaction = Transaction(sender, amount, receiver);
            sender.withdraw(amount);
            receiver.deposit(amount);
            cls.addTransaction(transaction);
            return transaction;
