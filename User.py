from abc import ABC, abstractmethod;
from Bank import Bank;

class User(ABC) :
    def __init__(self, name, email, address) -> None:
        self.name = name;
        self.email = email;
        self.address = address;
        self.debt = 0;
        self.loan_count = 2;
        self.trx_history = [];

    @abstractmethod
    def deposit(self, amount) :
        raise NotImplementedError;

    @abstractmethod
    def withdraw(self, amount) :
        raise NotImplementedError;

    @abstractmethod
    def checkBalance(self, amount) :
        raise NotImplementedError;

    @abstractmethod
    def transfer(self, amount, acc_no) :
        raise NotImplementedError;

    @abstractmethod
    def issueLoan(self, amount) :
        raise NotImplementedError;