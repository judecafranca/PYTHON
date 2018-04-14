#MIDTERM by Jude Cafranca

def match_a():
    print ("Function match_a() \n")

    jude1 = input("Enter 1st input:")
    jude2 = input("Enter 2nd input:")
    jude3 = input("Enter 3rd input:")

    jude22 = []
    jude33 = []
    jude11 = []

    for i in jude:
        if len(i) != 1:
            if i == i[::-1]:
                jude11.append(i)

    for i in jude2:
        if len(i) != 1:
            if i == i[::-1]:
                jude22.append(i)

    for i in jude3:
        if len(i) != 1:
            if i == i[::-1]:
                jude33.append(i)

    print ("1st output: ", len(jude11))
    print("2nd output: ", len(jude22))
    print ("3rd output: ", len(jude33))


match_a()
print ("\n\n")


def front_x():
    print ("Function front_x()\n")

    jude1 = input("Enter 1st input:")
    jude2 = input("Enter 2nd input:")
    jude3 = input("Enter 3rd input:")

    jude11 = []
    jude111 = []
    jude22 = []
    jude222 = []
    jude33 = []
    jude333 = []

    for i in jude1:
        if i.startswith('x'):
            jude11.append(i)
        else:
            jude111.append(i)

    print ("1st output: ", sorted(jude11) + sorted(jude111))

    for i in jude2:
        if i.startswith('x'):
            jude22.append(i)
        else:
            jude222.append(i)

    print ("2nd output: ", sorted(jude22) + sorted(jude222))

    for i in jude3:
        if i.startswith('x'):
            jude33.append(i)
        else:
            jude333.append(i)

    print ("3rd output: ", sorted(jude33) + sorted(jude333))


front_x()