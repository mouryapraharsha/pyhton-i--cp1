# finding number of letters and digits in a sentence

s = input("Input a string") #enter a string
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l) #print for number of letters
print("Digits", d)  #print for number of digits