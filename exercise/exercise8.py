print("Rock Paper Scissors game")
def compare(p1,p2):
    if p1==p2:
        return "Its a tie"
    elif p1=="rock":
        if p2=="scissors":
            return "Player 1 won"
        else:
            return "Player 2 won"
    elif p1=="scissors":
        if p2=="rock":
            return "Player 2 won"
        else:
            return "Player 1 won"
    else:
        if p2=="rock":
            return "Player 1 won"
        else:
            return "Player 2 won"


while True:
    player1=input("Enter your sign:").lower()
    player2=input("Enter your sign:").lower()
    print(compare(player1,player2))
    cont=input("Do you want to continue games y/n?")
    if cont=="y":
        continue
    else:
        break


