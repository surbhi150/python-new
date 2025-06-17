l="Good Morning, My name is Surbhi"
l1 = (l.split())
result= [i for i in l1 if len(i)<4]
print(result)

print("------------------------")
print("------------------------")

l2=['even' if i%2==0 else 'odd' for i in range(20)]
print(l2)

print("------------------------")
print("------------------------")

l3= [i for i in range(1,1000) if i%7==0]
print(l3)

print("------------------------")
print("------------------------")

l4="hey my name is surbhi I am a student pursuing Btech in computer science and artificial intelligence"
l5 = len([i for i in l4 if i==" "])
print(l5)

print("------------------------")
print("------------------------")

l6 = [1,2,3,4]
l7 = [2,3,4,5]
l8 = [i for i in l6 for j in l7 if i==j]
print(l8)