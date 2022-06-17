class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
s1 = Singleton()

print(id(s), id(s1))
assert id(s) == id(s1)