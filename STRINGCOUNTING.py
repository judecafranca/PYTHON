s = input("Input a string: ")
Dig=Let=0
for c in s:
    if c.isdigit():
        Dig=Dig+1
    elif c.isalpha():
        Let=Let+1
    else:
        pass
print("Letters", Let)
print("Digits", Dig)
