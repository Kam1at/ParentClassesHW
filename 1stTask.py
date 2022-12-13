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
        else: return True


    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"

print(Item("Phone", 18000, 5))