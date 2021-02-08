import random

a = random.randint(1, 9)
kiek=0;
while True:
    inpt=input("Guess the number:")
    if inpt=="exit":
        break
    if inpt.isnumeric():
        if a==int(inpt):
            print("Corect, you did",kiek,"guesses")
            print("Play again")
            a = random.randint(1, 9)
            kiek=0;
        else:
            kiek += 1
            if int(inpt)>a:
                print("To high")
            else:
                print("To low")
    else:
        print("Enter the number or exit")

