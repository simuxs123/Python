a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
c=[]
for i in range(len(a)):
    if a[i]<5:
        b.append(a[i])

print(b)

num=int(input("Enter number: "));
for i in range(len(a)):
    if a[i]<num:
        c.append(a[i])

print(c)
