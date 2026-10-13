a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))
if a>b:
    if b>c:
        print(a,">",b,">",c)
    else:
        if c>a:
            print(c,">",a,">",b)
        else:
            print(a,">",c,">",b)
else:
    if a>c:
        print(b,">",a,">",c)
    else:
        if c>b:
            print(c,">",b,">",a)
        else:
            print(b,">",c,">",a)
print("Program Executed !!!")
