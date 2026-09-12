positive=0
negative=0
zero=0
for i in range(5):
    num=int(input("enter a number"))
    if num>0:
        positive+=1
    elif num<0:
        negative+=1
    else:
        zero += 1
        print("positive number:",positive)
        print("negative number:",negative)
        print("zero number:",zero)
