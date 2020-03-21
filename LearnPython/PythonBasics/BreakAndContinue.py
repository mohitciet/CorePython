# break keyword

CountryList=["india","US","UK","Japan"]
for i in range(len(CountryList)):
    print(CountryList[i])
    if(CountryList[i]=="UK"):
        print(" UK found")
        break

print("===================")

# continue keyword

CountryList=["india","US","UK","Japan"]
for i in range(len(CountryList)):
    print(CountryList[i])
    if(CountryList[i]=="UK"):
        print(" UK found")
        continue