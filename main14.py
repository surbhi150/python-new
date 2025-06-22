a=input("Enter a string: ")
if len(a)<=2:
    print("The string is too short")
else:
    print(a[:2]+a[-2:])

print("-------------------------------")
print("-------------------------------")

b=input("Enter a string: ")
c=input("Enter another string:")
d=b.replace(b[0],c[0])
e=c.replace(c[0],b[0])
print(d,"",e)

print("-------------------------------")
print("-------------------------------")

f=input("Enter a string: ")
if len(f)<3:
    print("The string is too short")
elif len(f)==3:
    print(f)
elif f.endswith("ing"):
    print(f+"ly")
else:
    print(f+"ing")

print("-------------------------------")
print("-------------------------------")

g=input("Enter a string: ")
if len(g)==0:
    print("The string is empty")
else: 
    g.endswith(len(g)-1)