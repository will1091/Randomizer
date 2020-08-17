#!/usr/bin/python3

import string
import random
import sys

def randomizer(size, chars):
    return ''.join(random.choice(chars) for _ in range(int(size)))

def crunch(word):
    randlist=[]
    num=(string.digits)
    cap=(string.ascii_uppercase)
    low=(string.ascii_lowercase)

    for cont in word:
        if cont == "%": 
            cont=random.choice(num)
        elif cont == "@":
            cont=random.choice(low)
        elif cont == "&":
             cont=random.choice(cap)
        randlist.append(cont)

    print("".join(randlist))

def banner():
    
    print("                      _                 _              ")
    print("                     | |               (_)             ")
    print("  _ __ __ _ _ __   __| | ___  _ __ ___  _ _______ _ __ ")
    print(" | '__/ _` | '_ \ / _` |/ _ \| '_ ` _ \| |_  / _ \ '__|")
    print(" | | | (_| | | | | (_| | (_) | | | | | | |/ /  __/ |   ")
    print(" |_|  \__,_|_| |_|\__,_|\___/|_| |_| |_|_/___\___|_|   ")
    print("                                                       ")
    print("                                  by:  Me              ")
    print("                                                       ")


def proc(opc):
    if (opc=="1"):
        print("\n")
        banner()
        print("\n")
        print("          [    Digits   ]")
        chars=string.digits
        print("\n")
        ch_size = input("Characters size: ")
        num_str = input("Number of strings: ")
        print("\n")


        print("[      --       ]")
        print("\n")

        for cont in range(int(num_str)):
            print(randomizer(ch_size, chars))

    if (opc=="2"):
        print("\n")
        banner()
        print("\n")
        print("          [    Lowercase   ]")
        print("\n")
        chars=string.ascii_lowercase
        ch_size = input("Characters size: ")
        num_str = input("Number of strings: ")
        print("\n")
        print("[      --       ]")
        print("\n")

        for cont in range(int(num_str)):
            print(randomizer(ch_size, chars))

    if (opc=="3"):
        print("\n")
        banner()
        print("\n")
        print("          [    Uppercase   ]")
        print("\n")
        chars=string.ascii_uppercase
        ch_size = input("Characters size: ")
        num_str = input("Number of strings: ")
        print("\n")
        print("[      --       ]")
        print("\n")

        for cont in range(int(num_str)):
            print(randomizer(ch_size, chars))

    if (opc=="4"):
        print("\n")
        banner()
        print("\n")
        print("          [    Digits - Lowercase   ]")
        print("\n")
        chars=(string.digits+string.ascii_lowercase)
        ch_size = input("Characters size: ")
        num_str = input("Number of strings: ")
        print("\n")
        print("[      --       ]")
        print("\n")

        for cont in range(int(num_str)):
            print(randomizer(ch_size, chars))

    if (opc=="5"):
        print("\n")
        banner()
        print("\n")
        print("          [    Digits - Uppercase   ]")
        print("\n")
        chars=(string.digits+string.ascii_uppercase)
        ch_size = input("Characters size: ")
        num_str = input("Number of strings: ")
        print("\n")
        print("[      --       ]")
        print("\n")

        for cont in range(int(num_str)):
            print(randomizer(ch_size, chars))

    if (opc=="6"):
        print("\n")
        banner()
        print("\n")
        print("          [    Lowercase - Uppercase   ]")
        print("\n")
        chars=(string.ascii_lowercase+string.ascii_uppercase)
        ch_size = input("Characters size: ")
        num_str = input("Numbers of strings: ")
        print("\n")
        print("[      --       ]")
        print("\n")

        for cont in range(int(num_str)):
            print(randomizer(ch_size, chars))

    if (opc=="7"):
        print("\n")
        banner()
        print("\n")
        print("          [    Digits - Lowercase - Uppercase   ]")
        print("\n")
        chars=(string.digits+string.ascii_lowercase+string.ascii_uppercase)
        ch_size = input("Characters size: ")
        num_str = input("Number of strings: ")
        print("\n")
        print("[      --       ]")
        print("\n")

        for cont in range(int(num_str)):
            print(randomizer(ch_size, chars))

    if (opc=="8"):
        print("\n")
        banner()
        print("\n")
        print("                         [    Static word    ]")
        print("")
        print("  \"%\" - Numbers  --  \"&\" - Uppercase  --  \"@\" - Lowercase  ",end="\n")
        print("")
        print("                       eg. Cookie:%%&%@%%@@&          ")
        print("\n")
        
        word = input("Word:  ")
        num_str = input("Number of strings:    ")
        print("\n")

        for cont in range(int(num_str)):
            crunch(word)


def help():
    print("\n")
    print("randomizer -- random string generator", end="\n")
    print("usage: randomizer.py [option]")
    print("eg. randomizer.py 1")
    print("")
    print("[    --  Options  --    ]")
    print("")
    print("[1] Digits [0-9]")
    print("[2] Ascii lower cases [a-z]")
    print("[3] Ascii upper cases [A-Z]")
    print("[4] Digits & lower cases")
    print("[5] Digits & upper cases")
    print("[6] Lower cases & upper cases")
    print("[7] Digits, lower cases y upper cases")
    print("[8] Words")
    print("\n")



while True:
    try:
        opc=sys.argv[1]

        if len(sys.argv)!=2:
            help()
            break
        else:
            proc(opc)
            print("\n")
            break

        print("\n")
    except:
        help()
        break

