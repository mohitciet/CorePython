s1="Mohit"
s2="Singla"
s3="this is my home"

# concatination
print(s1+" "+s2)

# in, not in
print("is" in s3)
print("house" in s3)
print("house" not in s3)

# Writing String in Multiple Lines
s4= """ this is my class
this test
python
java
class """
print(s4)

# Writing string literals
s5= 'I\'m singla'
print(s5)

s6= "I am Test \"Engineer\""
print(s6)


# Capitalize
s7= 'this is a cat'
print(s7.capitalize())

# Find Method (Returns Index)
s7= 'this is a cat'
print(s7.find('this'))

# String Length
s8= 'this is a cat'
print(len(s8))

# String Length
s9= 'THIS is a Cat'
print(s9.lower())

# Trim String
s10= "  Hello  "
print(s10)
print("123"+s10.strip() + "123")

# Replace String
s11= "Sachin is a Footballer"
print(s11.replace("Footballer","cricketer"))


# Split String
s12= "Sachin is a Footballer"
print(s12.split(" "))
s12= "Sachin,is,a,Footballer"
print(s12.split(","))

# Reverse Ordering
s13= "Python"
print(s13[-1])
print(s13[-6])

# String Compare

s14="Test"
s15="Test"
print (s14 is s15) #check reference identification
print (s14==s15)   #Compare value

