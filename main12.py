name = input("Enter Student Name:  ")
classs = input("Enter Student Class:  ")
section = input("Enter Student Section:  ")
eng = int(input("Enter marks scored in English:  "))
mth = int(input("Enter marks scored in Maths:  "))
phy = int(input("Enter marks scored in Physics:  "))
chem = int(input("Enter marks scored in Chemistry:  "))
pun = int(input("Enter marks scored in Punjabi:  "))
marks = int(eng+mth+phy+chem+pun)
percentage = int(marks*100/500)
print(name)
print(classs)
print(section)
print(marks)
print(percentage)

print("------------------")
print("------------------")

a=int(input("Num1"))
b=int(input("Num2"))
c=int(input("Num3"))
summ = int(a+b+c)
print(summ)

print("------------------")
print("------------------")


d= int(input("Enter a number:  "))
sqr = int(d*d)
print(sqr)

print("------------------")
print("------------------")

temp = input("Temperature in celsius  ")
print(temp,"C")

print("------------------")
print("------------------")

temp = float(temp)
print(temp,"C")

print("------------------")
print("------------------")

frh = float((temp*9/5)+32)
print(frh,"F")

print("------------------")
print("------------------")

print(temp,"C")
print(frh,"F")

print("------------------")
print("------------------")

g=int(input("Enter number1  "))
h=int(input("Enter number2  "))
rem = int(g%h)
print(rem)

print("------------------")
print("------------------")

quo = float(g/h)
quo1 = int(g//h)
print("Quotient is: ",quo," , ",quo1)
print("Remainder is: ",rem)

print("------------------")
print("------------------")