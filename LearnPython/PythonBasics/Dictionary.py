"""DICTIONARY"""

dictionary={'key1' : 'india','key2' : 'USA'}

#Access Elements from Dictionary
print(dictionary['key1'])
print("===================")

#Adding Elements from Dictionary

dictionary={'key1' : 'india','key2' : 'USA'}
dictionary['key3']='Pakistan'
print(dictionary)

print("===================")

#Modify Elements from Dictionary

dictionary={'key1' : 'india','key2' : 'USA','key3':'Pakistan'}
dictionary['key3']='Aus'
print(dictionary)

print("===================")

#Delete  Elements from Dictionary

dictionary={'key1' : 'india','key2' : 'USA','key3':'Pakistan'}
del dictionary['key3']
print(dictionary)
print("===================")

#Looping to Iterate the Dictionary

dictionary={'key1' : 'india','key2' : 'USA','key3':'Pakistan'}
for x in dictionary:
    print(x +" : "+dictionary[x])

print("===================")


#Length of a Dictionary

dictionary={'key1' : 'india','key2' : 'USA','key3':'Pakistan'}
print(len(dictionary))

print("===================")


#Equallity Test in  Dictionary

dictionary1={'key1' : 'india','key2' : 'USA','key3':'Pakistan'}
dictionary2={'key1' : 'india','key2' : 'USA','key3':'Pakistan'}
dictionary3={'key1' : 'india','key2' : 'USA'}

print(dictionary1==dictionary2)
print(dictionary1==dictionary3)

print("===================")


#Functions in Dictionary

dictionary={'key1' : 'india','key2' : 'USA','key3':'Pakistan'}
print(dictionary.popitem()) #Returns random element and removed from Dictionary
print(dictionary)
print("===================")

dictionary={'key1' : 'india','key2' : 'USA','key3':'Pakistan'}
print(dictionary.keys()) #Returns all keys as tuple Format
print("<><><><>")
print(dictionary.values()) #Returns all values as tuple Format
print("<><><><>")
print(dictionary.get('key1')) #Returns value on the basis of key,if key invalid it returns None
print("<><><><>")
print(dictionary.pop('key5')) #Delete value on the basis of key,if key invalid it throws exception
print("<><><><>")
print(dictionary.clear()) #Delete Everything from Dictionary
print(dictionary)
print("<><><><>")
print("===================")