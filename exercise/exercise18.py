import random


def get_input(text):
    return input(text)


def count(c,b,nmb):
    for i in range(len(nmb)):
        if nmb[i] in number:
            if nmb[i] ==number[i]:
                c+=1;
            else:
                b+=1;
    return [c,b]

number = str(random.randint(0,9999))
c=0
b=0;

while True:
    inpt = get_input("Enter number: ")
    result=count(c,b,inpt);
    if inpt=="exit":
        break
    if result[0]==4:
        print("Congratulations, you won")
        break
    else:
        print("cows:",result[0],", bulls: ",result[1])
        c = 0
        b = 0



