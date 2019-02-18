
print([x**2 for x in range(1, 11)])


class Herobrine: #simple class
    def f():
        return "hello world"

e = Herobrine.f() #accessing class variables
print(e)


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name   #instance variable unique to each instance

d = Dog("Fido")
print(d.kind)
print(d.name)
