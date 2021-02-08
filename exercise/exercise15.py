def enter_question(text):
    return input(text)

def reverse_string(str):
    splt=str.split();
    return  " ".join([splt[i] for i in range(len(splt)-1,-1,-1)])


qst=enter_question("Enter long string containing multiple words: ")
print(reverse_string(qst))