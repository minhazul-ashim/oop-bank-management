from Bank import Bank;
from Account import SavingsAccount, CurrentAccount;

class SystemInteraction :
    @classmethod
    def accountCreation(cls) :
        print('Which account do you want to open?');
        print('1 - Savings Account');
        print('2 - Current Account');
        print('Go to ', end=' ');
        op = int(input());
        print('');
        print('Enter your name', end=" ");
        name = input();
        print('Enter your email', end=' ');
        email = input();
        print('Enter your address', end=' ');
        address = input();
        account = None;
        if(op == 1) :
            account = SavingsAccount(name, email, address);
            Bank.createAccount(account, op);
        elif(op == 2) :
            account = CurrentAccount(name, email, address);
            Bank.createAccount(account, op);
        else :
            print('Invalid Option');
        cls.userInteraction(account);
    
    @classmethod
    def userLogin(cls) :
        print('Enter your account number', end=' ');
        acc_num = input();
        account = Bank.authorizeUser(acc_num);
        if account :
            cls.userInteraction(account);
        else :
            print('Invalid Account Number');
    
    @classmethod
    def userInteraction(cls, account):
        while True :
            print(f'\n Welcome {account.name}, AC/NO: {account.acc_no}');
            print(f'Choose Option');
            print(f'1 - Check Balance');
            print(f'2 - Check Transaction');
            print(f'3 - Withdraw Cash');
            print(f'4 - Deposit Cash');
            print(f'5 - Transfer money to other account');
            print(f'6 - Take a loan');
            print(f'7 - Go Back');
            print('Go to ', end=' ');
            x = int(input());
            if x == 1 :
                print(f'Current Account Balance is {account.balance}');
            elif x == 2 :
                account.viewTransactions();
            elif x == 3 :
                print('Enter Withdraw Amount');
                amount = int(input());
                account.withdraw(amount);
            elif x == 4 :
                print('Enter Deposit Amount');
                amount = int(input());
                account.deposit(amount);
            elif x == 5 :
                print('Enter Receiver AC/NO', end=' ');
                receiver_no = input();
                print('Enter Amount', end=' ');
                a = int(input());
                account.transfer(a, receiver_no);
            elif x == 6 :
                print('Enter loan amount');
                amount = int(input());
                account.issueLoan(amount);
            elif x == 7 :
                break;
            else :
                print('Invalid Option');
    
    @classmethod
    def adminInteraction(cls) :
        while True :
            print(f'\n Welcome to Admin Dashboard\n');
            print(f'Choose Option');
            print(f'1 - Create Account');
            print(f'2 - Delete Account');
            print(f'3 - View All Accounts');
            print(f'4 - Check available balance');
            print(f'5 - Check loan amount');
            print(f'6 - Turn off/on loan feature');
            print(f'7 - Go Back');
            print('Go to ', end=' ');
            x = int(input());
            if x == 1 :
                print('Which account do you want to open?');
                print('1 - Savings Account');
                print('2 - Current Account');
                print('2 - Current Account');
                print('Go to ', end=' ');
                op = int(input());
                print('');
                print('Enter name', end=" ");
                name = input();
                print('Enter email', end=' ');
                email = input();
                print('Enter address', end=' ');
                address = input();
                account = None;
                if(op == 1) :
                    account = SavingsAccount(name, email, address);
                    Bank.createAccount(account, op);
                elif(op == 2) :
                    account = CurrentAccount(name, email, address);
                    Bank.createAccount(account, op);
                else :
                    print('Invalid Option');
            elif x == 2 :
                print('Enter account number to remove.');
                acc_no = input();
                Bank.removeAccount(acc_no);
            elif x == 3 :
                Bank.viewAccountList();
            elif x == 4 :
                print(f'Available balance is {Bank.getBalance()}')
            elif x == 5 :
                Bank.checkLoanAmount();
            elif x == 6 :
                Bank.toggleLoan();
            elif x == 7 :
                break;
            else :
                print('Invalid Option');