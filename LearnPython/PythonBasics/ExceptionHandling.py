print("Program Started")

try:
    #print(10/0)

    raise ArithmeticError

except TypeError:
    print("Inside Except block")
except BrokenPipeError:
    print("Inside Except block")
else:    #only executed if exception is not thrown
    print("Inside Else block")
finally:
    print("Always executed")

print("Program is completed")

