class Employee:

    __salary=1000 # Declaring Private Data Member

    def __disp(self):   #Private Method
        print("Private Method")

    def disp(self): #Public Method
        print(self.__salary)

e1=Employee()
e1.disp()  #Accessing Private Data Member through Public Method

e1._Employee__disp() # Access outside Class
print(e1._Employee__salary) #Accessing Private Data Member outside Class



