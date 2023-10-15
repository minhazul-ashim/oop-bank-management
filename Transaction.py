from datetime import datetime;

class Transaction :
    def __init__(self, sender, amount, receiver) -> None:
            self.sender = sender;
            self.receiver = receiver;
            self.amount = amount;
            self.time = datetime.now();
            