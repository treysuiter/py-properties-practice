class Product():

    def __init__(self, name):
        self.onSale = False
        self.name = name

    @property  # The getter
    def price(self):
        try:
            return self.__price  # Note there are 2 underscores here
        except AttributeError:
            return 0

    @price.setter  # The setter
    def price(self, new_price):
        if type(new_price) is float:
            self.__price = new_price
        else:
            raise TypeError(
                'Please provide a floating point value for the price')

    def __str__(self):

        if self.onSale:
            return f"The {self.name} costs ${'{:.2f}'.format(self.price)} What a deal!"
        else:
            return f"The {self.name} costs ${'{:.2f}'.format(self.price)} You getting ripped off."


# a_thing = Product()
# a_thing.price = 5.00

# print(a_thing.price)


car = Product("Mustang")

car.onSale = True
car.price = 1200.00

print(car)
