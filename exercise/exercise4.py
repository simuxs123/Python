num=int(input("Enter the number: "))
x=range(1,num+1);
a=[];
for i in x:
    if(num%i==0):
        a.append(i);

print(a)