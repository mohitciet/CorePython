#Collection data type : List
#List is Indexed,ordered,Mutable(Content can be changed),Duplicate values Allowed,Data can be appended

score=[1,2,3,4,5,5]
print(score)
print(score[0])
print(score[4])
print(score[-1])
print(score[-5])

#Forward Traversal  :  0-4
#Backward Traversal  :  -1 - -5

# Shallow/Copy of Lists
score=[2,1,3,4,5,6]
print(score[:])
score1=score[:]
print(score1)

#  Lists Concatination
score2=[1,2,3,4,5]
print(score2+['a','b','c'])

#  Lists are Mutable
score3=[1,2,3,4,5]
score3[2]="updated Value"
print(score3)

# append
score4=[1,2,3,4,5]
score4.append(100)
print(score4)

name=['a','b','c','d','e']
name[2:5]=["A","B","C"] # Modify List
print(name)

name[:]=[]    #Empty List
print(name)


# Length of List
score5=[1,2,3,4,5]
print(len(score5))

#nested Lists
a1=[1,2,3]
a2=['A','B']
x=[a1,a2]
print(x)
print(x[0])
print(x[1])
