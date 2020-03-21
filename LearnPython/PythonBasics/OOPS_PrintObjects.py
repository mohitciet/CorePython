# string representation of class objects

class Test:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    # def __str__(self):
    #     print("Str Method is called")
    #     return "value of x:%s and value of y:%s" %(self.x,self.y)
    def __repr__(self):
        print("repr Method is called")
        return "value of x:%s and value of y:%s" % (self.x, self.y)

t1=Test(1,2)
print(t1)