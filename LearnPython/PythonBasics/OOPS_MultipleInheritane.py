#Python Supports Multiple Inheritance
class Base1:

    def __init__(self):
        self.name="Mohit"
        print("Base1 class Constructor")


class Base2:

    def __init__(self):
        self.roll = "Singla"
        print("Base2 class Constructor")

class Child(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

        print("Child Constructor")

    def printStrings(self):
        print(self.name,self.roll)

c1=Child()
print(c1.printStrings())
