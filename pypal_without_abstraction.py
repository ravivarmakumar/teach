class PyPalAccount:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


def main():
    Ravi = PyPalAccount("ravi", 100)
    Bhanu = PyPalAccount("Bhanu", 1000)

    # Ravi gets his paycheck and deposits it
    Ravi.amount += 500

    # Bhanu wants to buy a new enclosure for her chickens
    Bhanu.amount -= 900

    # Ravi wants to travel to Costa Rica to hang out with sloths
    Ravi.amount -= 2000
    # Bad! There is no guarantee that Ravi has enough money to do that!

    # Ravi wants to transfer some money to Bhanu for lunch
    Bhanu.amount += 20
    # Bad! The money appeared out of nowhere!

    # Identity fraud (bad)
    Ravi.name = "Bhanu"


if __name__ == '__main__':
    main()