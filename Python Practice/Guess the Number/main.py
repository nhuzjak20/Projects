import random

broj = random.randint(0,30)
zivoti = 4

ime = input("Unesi ime: ")

while(zivoti >= 0):
    pogodak = int(input("Pogodi broj izmedu 0 i 30: "))
    if pogodak > broj:
        zivoti = zivoti - 1
        print("Pogodili ste preveliki broj, imate " + str(zivoti) + " pokusaja")
    elif pogodak < broj:
        zivoti = zivoti - 1
        print("Pogodili ste premali broj, imate " + str(zivoti) + " pokusaja")
    elif pogodak == broj:
        print("Cestitam, pogodili ste broj i ostalo vam je " + str(zivoti) + " pokusaja")
        exit()
    elif zivoti == 0:
        print("Nemate vise zivota")
        exit
