class Person(object):

    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False

p1= Person("Harry")
print(p1.getName())
print(p1.isEmployee())

print("================")

class ChildClass(Person):

    def isEmployee(self):
        return True

c1=ChildClass("Tom")
print(c1.getName())
print(c1.isEmployee())  #Method Overiding

#Method Overloading

class Human :

    def getName(self,name=None):
        if name is None:
            print("First Case")
        else:
            print("Second Case")

h1=Human()
h1.getName()
h1.getName("A")




