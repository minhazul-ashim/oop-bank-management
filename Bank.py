class Bank :
    __saving_accounts = [];
    __current_accounts = [];
    __balance = 0;
    __loan = False;
    __trx_history = [];
    __loan_issued = 0;
    __loan_amount = 0;

    @classmethod
    def checkLoanAmount(cls) :
        return (cls.__loan_amount, cls.__loan_issued);

    @classmethod
    def toggleLoan(cls) :
        cls.__loan = not cls.__loan;

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
    def removeAccount(cls) :
        pass;

    @classmethod
    def checkBankBalance(cls) :
        return cls.__balance;

    @classmethod
    def viewAccountList(cls) :
        return (cls.__current_accounts + cls.__saving_accounts);

    @classmethod
    def viewTransactins(cls) :
        return cls.__trx_history;

    @classmethod
    def authorizeUser(cls, acc_no) :
        for account in cls.__saving_accounts :
            if(account.acc_no == acc_no) :
                return account;
        for account in cls.__current_accounts :
            if(account.acc_no == acc_no) :
                return account;

        return None;