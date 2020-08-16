
#!/usr/bin/python3

import string
import random
import os

def randomizer(size, chars):
    return ''.join(random.choice(chars) for _ in range(int(size)))

def crunch(word):
    z=[]
    num=(string.digits)
    cap=(string.ascii_uppercase)
    low=(string.ascii_lowercase)

    for c in word:
        if c == "%": 
            c=random.choice(num)
        elif c == "@":
            c=random.choice(low)
        elif c == "&":
             c=random.choice(cap)
        z.append(c)

    print("".join(z))




print("                      _                 _              ")
print("                     | |               (_)             ")
print("  _ __ __ _ _ __   __| | ___  _ __ ___  _ _______ _ __ ")
print(" | '__/ _` | '_ \ / _` |/ _ \| '_ ` _ \| |_  / _ \ '__|")
print(" | | | (_| | | | | (_| | (_) | | | | | | |/ /  __/ |   ")
print(" |_|  \__,_|_| |_|\__,_|\___/|_| |_| |_|_/___\___|_|   ")
print("                                                       ")
print("                                  by:  Me              ")
print("                                                       ")



print("[      Options      ] ")

print(" ")
print("[1] Digits [0-9]")
print("[2] Ascii lowercase [a-z]")
print("[3] Ascii uppercase [A-Z]")
print("[4] Digits & lowercase")
print("[5] Digits & uppercase")
print("[6] Lowercase & uppercase")
print("[7] Digits, lowercase y uppercase")
print("[8] Words")
opc=input("\nOption: ")
os.system("clear")

if (opc=="1"):
    print("\n")
    print("          [    Digits   ]")
    chars=string.digits
    print("\n")
    x = input("Characters size: ")
    y = input("Number of strings:    ")
    print("\n")
    os.system("clear")


    print("[      --       ]")
    print("\n")

    for cont in range(int(y)):
        print(randomizer(x, chars))

if (opc=="2"):
    print("\n")
    print("          [    Lowercase   ]")
    print("\n")
    chars=string.ascii_lowercase
    x = input("Characters size:      ")
    y = input("Number of strings:    ")
    print("\n")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("\n")

    for cont in range(int(y)):
        print(randomizer(x, chars))

if (opc=="3"):
    print("\n")
    print("          [    Uppercase   ]")
    print("\n")
    chars=string.ascii_uppercase
    x = input("Characters size:      ")
    y = input("Number of strings:    ")
    print("\n")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("\n")

    for cont in range(int(y)):
        print(randomizer(x, chars))

if (opc=="4"):
    print("\n")
    print("          [    Digits - Lowercase   ]")
    print("\n")
    chars=(string.digits+string.ascii_lowercase)
    x = input("Characters size:      ")
    y = input("Number of strings:    ")
    print("\n")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("\n")

    for cont in range(int(y)):
        print(randomizer(x, chars))

if (opc=="5"):
    print("\n")
    print("          [    Digits - Uppercase   ]")
    print("\n")
    chars=(string.digits+string.ascii_uppercase)
    x = input("Characters size:      ")
    y = input("Number of strings:    ")
    print("\n")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("\n")

    for cont in range(int(y)):
        print(randomizer(x, chars))

if (opc=="6"):
    print("\n")
    print("          [    Lowercase - Uppercase   ]")
    print("\n")
    chars=(string.ascii_lowercase+string.ascii_uppercase)
    x = input("Characters size:      ")
    y = input("Numbers of strings:    ")
    print("\n")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("\n")

    for cont in range(int(y)):
        print(randomizer(x, chars))

if (opc=="7"):
    print("\n")
    print("          [    Digits - Lowercase - Uppercase   ]")
    print("\n")
    chars=(string.digits+string.ascii_lowercase+string.ascii_uppercase)
    x = input("Characters size:      ")
    y = input("Number of strings:    ")
    print("\n")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("\n")

    for cont in range(int(y)):
        print(randomizer(x, chars))

if (opc=="8"):
    print("\n")
    print("                         [    Static word    ]")
    print("")
    print("  \"%\" - Numbers  --  \"&\" - Uppercase  --  \"@\" - Lowercase  ",end="\n")
    print("")
    print("                       eg. Cookie:%%&%@%%@@&          ")
    print("\n")
    
    x = input("Word:  ")
    y = input("Number of strings:    ")
    print("\n")

    for c in range(int(y)):
        crunch(x)



print("\n")
print("\n")




