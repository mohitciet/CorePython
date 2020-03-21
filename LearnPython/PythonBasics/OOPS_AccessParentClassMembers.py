class Base:

    def __init__(self,x):
        self.x=x

class Child(Base):

    def __init__(self,x,y):
        Base.x=x
        self.y=y

    def printData(self):
        print ("x : "+Base.x)
        print("y : " + self.y)

ob=Child("a","b")
ob.printData()
