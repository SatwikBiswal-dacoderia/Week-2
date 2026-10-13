str=input("Enter the string : ")
a=input("Enter the letter you want to count : ")
c=0
flag=0
for i in str:
    if i==a:
        c+=1
        flag=1
print("The no of times ",a," occured is : ",c)
if flag==0:
    print(a," was not found")
else:
    print("Program executed")
