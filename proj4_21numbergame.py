import random


print("Welcome to 21 number game.")
lst=[0]
def compgen():
    fo=0
    num=lst[-1]
    word=random.randrange(1,4)
    
    sum=num+word
    if sum > 21:
        fo=1
        return fo
    else:
        for i in range(1,word+1):
            num=num + 1 
            lst.append(num)
    print("List after Computer's turn: ")
    print(lst)
    return fo  
def usergen():
    fop=0
    num=lst[-1]
    prn=int(input("How many words you want to enter?: (less than 4)"))
    word=prn+1
    sum=num+word
    if sum > 21:
        fop=1
        return fop
    else:
        for i in range(1,word):
            num=num + 1 
            lst.append(num)
    print("List after your turn: ")
    print(lst)
    return fop      
def loop1():
    flag=0
    while(flag==0):
        f=usergen()

        if(f==1):
            print("You Lost 1.1!!!")
            break;
        f=compgen()
        if(f==1):
            print("You Win 1.2!!!")
            break;    
def loop2():
    flag=0
    while(flag==0):
        f=compgen()
        if(f==1):
            print("You Win 2.1!!!")
            break;
        f=usergen()
        if(f==1):
            print("You Lost 2.2!!!")
            break;    
inp =int(input(("You want to go First or Second??? (1/2)")))
if inp==1:
    loop1()
else:
    loop2()
