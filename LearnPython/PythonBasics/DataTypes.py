#No need tod declare any type of variable
a=1
print(a)
a="Mohit"
print(a)
a=30.1
print(a)

#Two variables refering same location
x=123
print(id(x)) #print identity of x
y=x
print(id(y)) #print identity of y


#################
a1=1
a2=2
print(a1,a2)

a1,b1,c1=1,12.1,"Mohit"
print(a1,b1,c1)


s1="Hello World"
print(s1)
print(s1[0])
# print(s1[123]) # IndexError: string index out of range
print(s1[0:1])
print(s1*3)


