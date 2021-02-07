import datetime
name = input("Give me your name: ")
age=int(input("Give me your age: "));
repeat=int(input("How many times repeat message?: "));
date= datetime.datetime.now()
yearTurn100=100-age+date.year;
print(repeat*("Your name is " +name+"  and you will turn 100 years old on "+str(yearTurn100)+"\n"))
