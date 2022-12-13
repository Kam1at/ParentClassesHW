class Item:
    def __init__(self, name, price, quantity=0):
        self.__check(name, price, quantity)
        self.name = name
        self.price = price
        self.quantity = quantity

    def __check(self, name, price, quantity):
        if not isinstance(name, str):
            raise TypeError(": Название товара должно быть строкой.")
        elif not isinstance(price, int):
            raise TypeError(": Цена товара должна быть числом.")
        elif not isinstance(quantity, int):
            raise TypeError(": Количество товара должно быть целым числом.")
        else:
            return True

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"


class Phone(Item):
    broken_phones = 0

    def __init__(self, a, b, c, d):
        Item.__init__(self, name=a, price=b, quantity=c)
        if type(d) is int:
            self.broken_phones += d
        else:
            raise TypeError(": Количество должно быть цифрой.")

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity}, {self.broken_phones})"

print(Item("Phone", 18000, 5))
phone1 = Phone("iPhone 10", 500, 5, 1)
print(phone1.broken_phones)
print(phone1)