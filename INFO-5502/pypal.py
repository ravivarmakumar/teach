class PyPalAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def deposit(self, deposit_amount):
        """
        Allows the user to deposit a positive amount of money
        into their account. Returns whether or not the 
        deposit was successful.
        """
        if deposit_amount < 0:
            print("Sorry, you can't deposit negative money!")
            return False
        self.amount += deposit_amount
        return True

    def withdraw(self, withdrawal_amount):
        """
        Allows the user to withdraw some amount of money
        from their account. Returns whether or not the 
        withdrawal was successful.
        """
        if withdrawal_amount < 0:
            print("Sorry, you can't withdraw negative money!")
            return False
        elif withdrawal_amount > self.amount:
            print("Sorry, you don't have enough money in your account to do that!")
            return False
        else:
            self.amount -= withdrawal_amount
            return True

    def transfer(self, recipient, transfer_amount):
        """
        Allows the user to transfer a certain amount of money to 
        a recipient, represented as another PyPalAccount object. Returns
        whether or not the transfer was successful.
        """
        success = self.withdraw(transfer_amount)
        if success:
            return recipient.deposit(transfer_amount)
        else:
            print("Wasn't able to make the necessary withdrawal, terminating transfer")
            return False

    def get_amount(self):
        return self.amount

    def get_name(self):
        return self.name


def main():
    Ravi = PyPalAccount("Ravi", 100)
    Bhanu = PyPalAccount("Bhanu", 1000)

    # Ravi gets his paycheck and deposits it
    Ravi.deposit(500)

    # Bhanu wants to buy a new enclosure for her chickens
    Bhanu.withdraw(900)

    # Ravi wants to travel to Costa Rica to hang out with sloths
    Ravi.withdraw(2000)
    # Oops, not enough money! But account status is still valid
    print(Ravi.get_amount())

    # Ravi wants to transfer some money to Bhanu for lunch
    Ravi.transfer(Bhanu, 20)

    print(Ravi.get_name(), Ravi.get_amount())
    print(Bhanu.get_name(), Bhanu.get_amount())


if __name__ == '__main__':
    main()
