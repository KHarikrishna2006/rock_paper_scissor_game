import random as r
print("\t\t\t\t\t\tRock Paper Scissor\n")
print("Rules of Game : \n")
print("1.Rock VS Paper ====> Paper wins\n2.Rock VS Scissor ====> Rock wins\n3.Scissor VS Paper ====> Scissor wins\n\n")
print("==>A win in each round gains a point.\n==>Gaining 3 points declares the WINNER.\n\n")
name=input("Enter your name:\n")
possibilities=["rock","paper","scissor"]
print("let's Begin the Game\n")
ch='Y'
cl=0
hl=0
while(ch=='Y'):
    print("1.Rock\n2.Paper\n3.Scissor\n")
    choice=int(input("Enter your Choice:"))
    a=possibilities[choice-1]
    b=r.choice(possibilities)
    print("Your Choice is:"+a)
    print("Computr's choice:"+b)
    print(a," VS ",b)
    if(a=="rock" and b=="scissor"):
        print(name," win's\n")
        hl+=1
        print("Points ==> computer= ",cl,"\t\t",name,"= ",hl)
    if(a=="rock" and b=="paper"):
        print("Computer win's\n")
        cl+=1
        print("Points ==> computer= ",cl,"\t\t",name,"= ",hl)
    if(a=="paper" and b=="scissor"):
        print("Computer win's\n")
        cl+=1
        print("Points ==> computer= ",cl,"\t\t",name,"= ",hl)
    if(a=="paper" and b=="rock"):
        print(name," win's\n")
        hl+=1
        print("Points ==> computer= ",cl,"\t\t",name,"= ",hl)
    if(a=="scissor" and b=="rock"):
        print("computer win's\n")
        cl+=1
        print("Points ==> computer= ",cl,"\t\t",name,"= ",hl)
    if(a=="scissor" and b=="paper"):
        print(name," win's\n")
        hl+=1
        print("Points ==> computer= ",cl,"\t\t",name,"= ",hl)
    if(a=="scissor" and b=="scissor"):
        print("It'a a tie.")
        print("Points ==> computer= ",cl,"\t\t",name,"= ",hl)
    if(a=="rock" and b=="rock"):
        print("It'a a tie.")
        print("Points ==> computer= ",cl,"\t\t",name,"= ",hl)
    if(a=="paper" and b=="paper"):
        print("It'a a tie.")
        print("Points ==> computer= ",cl,"\t\t",name,"= ",hl)
    if(cl==3 or hl==3):
        if(hl==3):
            print("------",name," Win's------")
        else:
            print("------Computer Win's------")
        ch=input("Do you want to play again!!\nYES=Y\nNO=N")
