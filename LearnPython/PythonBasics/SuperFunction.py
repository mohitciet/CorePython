a,b=21,22

class A:
    a,b=1,2
    def __init__(self):
        print("Parent class constructor")

    def m1(self):
        print("m1 fn")

class B(A):

    a,b=11,12

    def __init__(self):
        super().__init__() #Invoking Parent Class Constructor
        print("Child class constructor")

    def m2(self):
        super().m1()  #Invoking Parent Class method
        print(super().a) #Invoking Parent Class variable
        print(super().b)
        print(self.a) #invoking child Case variables
        print(self.b)
        print("m2 fn")

b=B()
b.m2()
