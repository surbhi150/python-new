a= (3, 5, 1, 8, 2,10,2,5,15,76)
b=set(a)
c=tuple(b)
print(c)

Print("-----Question2--------")
Print("-----Question2--------")

a= [[1, 2], [3, 4], [5, 6]]
b=[]
for i in a:
    for j in i:
        b.append(j)
print(b)

Print("-----Question2--------")
Print("-----Question2--------")

d= (3, 5, 1, 8, 2)
e= (max(d))
f=(min(d))
print("The maximum value in the tuple is: ", e)
print("The minimum value in the tuple is: ", f)

Print("-----Question2--------")
Print("-----Question2--------")

g=(1,2,3,4,5)
h=[i*i*i for i in g]
ans = (list(zip(g,h)))
print(ans)
    
