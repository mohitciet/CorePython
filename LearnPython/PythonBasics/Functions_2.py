#Keyword Arguments
def login(username,password):
    print(username,password)

login(username="MohitTest",password="abc@123")

#Arbitrary Arguments, *args (When the number of arguments are unknown)
#This way the function will receive a TUPLE of arguments

def getMarks(*arg):
    for x in arg:
        print(x)

getMarks(1,2,3,4,5)
getMarks(1,2,3)

print("==============================")


#Arbitrary Arguments, **args (When the number of arguments are unknown)
#This way the function will receive a DICTIONARY of arguments


def getStudentMarks(**arg):
    for key,value in arg.items():
        print("%s==%s" %(key,value))

getStudentMarks(num1=1,num2=2)



#Python Lambda
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

cube=lambda x : x*x*x

print (cube(4))
