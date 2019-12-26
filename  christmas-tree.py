from random import randint
from time import sleep


rnd2 = randint(1, 30)


def prRed(prt): print("\033[91m {:^33}\033[00m" .format(prt))


def prGreen(prt): print("\033[92m {:^33}\033[00m" .format(prt))


def prYellow(prt): print("\033[93m {:^33}\033[00m" .format(prt))


def prLightPurple(prt): print("\033[94m {:^33}\033[00m" .format(prt))


def prPurple(prt): print("\033[95m {:^33}\033[00m" .format(prt))


def prCyan(prt): print("\033[96m {:^33}\033[00m" .format(prt))


def prLightGray(prt): print("\033[97m {:^33}\033[00m" .format(prt))


def prBlack(prt): print("\033[98m {:^33}\033[00m" .format(prt))


def gentree():
    print('\033c')
    for x in range(1, 30, 2):
        rnd1 = randint(1, rnd2)
        if x == 1:
            ch = '$'
        elif rnd1 % 4 == 0:
            ch = 'o'
        elif rnd1 % 3 == 0:
            ch = 'i'
        else:
            ch = '*'
        index = randint(1, 7)
        if index == 1:
            prRed(ch * x)
        elif index == 2:
            prGreen(ch * x)
        elif index == 3:
            prYellow(ch * x)
        elif index == 4:
            prLightPurple(ch * x)
        elif index == 5:
            prPurple(ch * x)
        elif index == 6:
            prCyan(ch * x)
        elif index == 7:
            prLightGray(ch * x)
        else:
            print("{:^33}".format(ch * x))
    print("{:^33}".format("|||"))
    print("{:^33}".format("|||"))
    prGreen("FELIZ NATAL")
    prGreen("MERRY CHRISTMAS")
    prGreen("FELIZ NAVIDAD")

    sleep(.75)


while True:
    gentree()
