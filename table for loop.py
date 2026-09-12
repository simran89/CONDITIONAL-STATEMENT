num=int(input("enter a number:(2 to 10):"))
if num>= 1 and num<= 10:
    for i in range(1,11):
        print(num,"X",i,"=",num*i)
    else:
        print("please enter a number between 1 and 10.")