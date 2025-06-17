num=int(input("Enter a number: "))
if num==1:
    print("January")
elif num==2:
    print("February")
elif num ==3:
    print("March")
elif num==4:
    print("April")
elif num==5:
    print("May")
elif num==6:
    print("June")
elif num==7:
    print("July")
elif num==8:
    print("August")
elif num==9:
    print("September")
elif num==10:
    print("October")
elif num==11:
    print("November")
elif num==12:
    print("December")
else:
 print("Invalid month")

print("----------------------")
print("----------------------")

num1= int(input("Enter a number: "))
num2 = int(input("Enter another number: ")) 
if num1>num2:
     print("First number is greater than second number")
     print("surbhi"*5)
elif num1<num2:
     print("First number is smaller than second number")
     print("surname"*3)
else:
     print("Both number are equal")


print("----------------------")
print("----------------------")

a=input("ENter name: ")
b=input("Enter another name: ")

if a==b:
    print("both are equal ==")
else:
    print("invalid")
print("Equality using is keyword", (a is b))

print("----------------------")
print("----------------------")

c= input("Enter a string: ")
e= input("Enter another string: ")
print(id(c))
print(id(e))
if c is e:
    print("both are same")
else:
    print("both are not same")


print("----------------------")
print("----------------------")


num3 = int(input("Enter number: "))
totalsum=0
for i in range(1,num3+1):
    totalsum+=i
print(totalsum)
    
print("----------------------")
print("----------------------")

num4 = int(input("Enter a number: "))
for i in range(1,num4+1):
    if i % 2 == 0:
        print(i)
print("----------------------")
print("----------------------")

num5 = int(input("Enter a number: "))
for i in range(1,num5,1):
    print(i, end=',')

for i in range(num5,1,-1):
 print(i)

print("----------------------")
print("----------------------")

num6 = int(input("Enter a number: "))
table=0
for i in range(1,num6+1):
    table = num6 * i
    print(f"{num6} * {i} = {table}")


print("----------------------")
print("----------------------")

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("----------------------")
print("----------------------")

num7 = int(input("Enter a number: "))
square = 0
for i in range(1,num7+1):
    square=i*i
    print(square)
