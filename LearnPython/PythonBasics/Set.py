#Set vs :List,Tuple
#not order based
#performs different mathematical calculations
#it does not store duplicate elements
#it is an object

# Unique Data
s1={1,2,3,1,2,3}
print(s1)

print("==============")

#set() Function
#tuple,list can be passed

s3=set("python")
print(s3)
print("==============")

# While Creating a set object ,you can store only Numbers,String,tuple
#List,Dictionary not allowed

# s3={[1,2]}
# print(s3)


# s3=set([1,2,3])
# print(s3)
print("==============")

# set Operations

p1={1,2,3,4}
p2={3,4,5,6}
print(p1|p2)  #Union
print(p1.union(p2))

print(p1&p2)
print(p1.intersection(p2)) #intersection

print(p1-p2) #difference of sets
print(p1.difference(p2))

print(p1^p2) #symmateric difference
print(p1.symmetric_difference(p2))

#Set-Inbuilt Methods

s1={"Java","C Sharp","Python","Javascript"}
s1.add("perl") #add
print(s1)

s1.update(["VB","123"])
print(s1)

s1={"Java","C Sharp","Python","Javascript"}
s2=s1.copy()  #copy
print(s2)

s1={"Java","C Sharp","Python","Javascript"}
s1.discard("Python")  #discard
print(s1)

s1={"Java","C Sharp","Python","Javascript"}
s1.remove("Python")  #remove (throws error on removing not present element)
print(s1)




