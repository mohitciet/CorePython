# while loop with else
num=0
while(num<3):
    print("number is : "+str(num))
    num=num+1
else:
    print("Comes out of Loop")

print("==================")

# for-loop (else can also be used)

name=["Java","Python","Perl","C sharp"]
for i in name:
    print(i)

print("==================")

list=["Mohit","is","a","boy"]
for index in range(len(list)):
    print(list[index])

print("==================")

# nested for loop
for i in range(1,5):
     for j in range(i):
         print(i,end='')
     print()

