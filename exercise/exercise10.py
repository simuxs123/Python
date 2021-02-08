import random

a = random.sample(range(20), 10)
b = random.sample(range(20), 15)
b=[i for i in list(set(a)) if i in list(set(b))]
print(b)


a = [1,1,2,3,4,4,5,5,]
b=[1,1,2,2,3,3,4,4,5,6,7,8,8]
b=[i for i in list(set(a)) if i in list(set(b))]
print(b)