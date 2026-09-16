#vowels
text=input("Enter a word")
count=0
for i in text:
    if i in "aeiouAEIOU":
        count+=1
print("number of vowels:",count)
