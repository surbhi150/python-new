l=[0,1,2,3,4,5,6,7,8,9]
print(l)

print("-----------------------")
print("-----------------------")

l1=[1,10,100,3,6,8]
l1.insert(3,59)
l1.append(5)
print(l1)
print(len(l1))

print("-----------------------")
print("-----------------------")

l2= [1,4,2,42,4,6,2,56,4,56,2]
for i in range(0,len(l2),2):
    print(l2[i])

print("-----------------------")
print("-----------------------")

l3=["Gaurav",12,23,33.33,"Sharma",True]
for i in l3:
    if type(i)==str:
        print(i)

print("-----------------------")
print("-----------------------")

l4=[1,4,2,42,4,6,2,56,4,56,2]
u=0
for i in l4:
    u+=i
print(u)

print("-----------------------")
print("-----------------------")

l5=[input("Enter your friend name: ")]
print(l5)