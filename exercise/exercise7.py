a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
newlist=[a[i] for i in range(len(a)) if a[i]%2==0 ]

print(newlist)