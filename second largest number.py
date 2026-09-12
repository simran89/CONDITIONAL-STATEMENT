number=[10,52,30,45,60,35,20,]
largest=number[0]
second=number[0]
for i in number:
    if i>largest:
        largest=i
        second=largest
        largest=i
    elif i>second and i !=largest:
        second=i
        print("second",second)
