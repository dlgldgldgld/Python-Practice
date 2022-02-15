class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
        print(f'{self.func=} {self.name=}')

    def __get__(self, instance, owner):
        print(f'__get__ called {owner=} {instance=}')
        if not instance :
            return self
        v = self.func(instance)
        instance.__dict__[self.name] = v
        return v

TAX_RATE = 1.10
class Book:
    def __init__ (self, raw_price):
        self.raw_price = raw_price
    @LazyProperty
    def price(self):
        print('calculate the price')
        return int(self.raw_price * TAX_RATE)

book = Book(1980)
print('first_call')
print(book)
print(book.price)
print('second_call')
print(book.price)