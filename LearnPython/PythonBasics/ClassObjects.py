#Self is like this Operator in JAVA (It holds Current Class object reference)

i,j=21,22 #Global Variables (Outside Class)

class Car:


    wheels=4 #class variables
    i,j=11,12

#Constructor of this class
#Constructor overloading is not allowed in Python
#It is mandatory to declare constructor
#Object only access the latest created Constructor

    def __init__(self,color):
        print("Car Class Constant 1")


    def testFunction(self):
        print("Method in a Class")

   #If any var is declared inside method : instance/local variable
    def setValue(self,price):   #instance Method
        self.price=price
    def getValue(self):
        return self.price

    #static Method
    #Python Does not have  static variable concept
    @staticmethod
    def staticMethod():
        print("Static Method")

    def sameNameVariables(self,i,j):
        print(i+j)  # Accessing Local Variables
        print(self.i+self.j) # Accessing Class Variables
        print(globals()['i']+globals()['j']) # Accessing Global Variables




c1= Car("Red")
c1.setValue("1000")
price=c1.getValue()
print(price)
print(Car.staticMethod())
print(c1.wheels)
print("Accessing Class variables with class Name : "+str(Car.i))

print("===============")
c1.sameNameVariables(1,2)

print(id(c1)) #Memory locations of Objects

del c1 #Destroying Objects

#Blank Class

class Person:
  pass

p1=Person()


