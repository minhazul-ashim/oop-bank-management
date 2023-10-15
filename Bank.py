class Bank :
    saving_accounts = [];
    current_accounts = [];
    balance = 0;
    loan = False;
    trx_history = [];
    loan_issued = 0;

    @classmethod
    def checkBankBalance(self) :
        return self.__balance;

    @classmethod
    def viewAccounts(self) :
        return self.__accounts;
