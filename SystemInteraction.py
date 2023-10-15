from Bank import Bank;
from Account import SavingsAccount, CurrentAccount;

class SystemInteraction :
    @classmethod
    def accountCreation(cls) :
        print('Which account do you want to open?');
        print('1 - Savings Account');
        print('2 - Current Account');
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
            print(f'\n Welcome {account.name}\n');
            print(f'Choose Option');
            print(f'1 - Check Balance');
            print(f'2 - Check Transaction');
            print(f'3 - Withdraw Cash');
            print(f'4 - Deposit Cash');
            print(f'5 - Transfer money to other account');
            print(f'6 - Go Back');
            print('Go to ', end=' ');
            x = int(input());
            if x == 1 :
                pass;
            elif x == 2 :
                pass;
            elif x == 3 :
                pass;
            elif x == 4 :
                pass;
            elif x == 5 :
                pass;
            elif x == 6 :
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
                pass;
            elif x == 2 :
                pass;
            elif x == 3 :
                pass;
            elif x == 4 :
                pass;
            elif x == 5 :
                pass;
            elif x == 6 :
                pass;
            elif x == 7 :
                break;
            else :
                print('Invalid Option');