#optional/default Parameters
def countryName (name="India"):
    print(name)

countryName()
countryName("Pakistan")

print("===========================")

#Passing List to a Function,return value from fn

def getNames (list):
    for i in list:
        if(i=="China"):
            print(i)
            return i

countryNames=["india","uk","Australia","China"]
getNames(countryNames)

print("===========================")

#Recursion in Python
def factorial(number):
    if(number>1):
        number=number*factorial(number-1)
    return number

print(factorial(5))

print("===========================")

#Login Example

def login(username,password):
    print("login with %s and %s" %(username,password))

login("Mohit","Singla")





