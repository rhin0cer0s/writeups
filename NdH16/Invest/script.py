#! /usr/bin/python3


def decode(buff):
    a = bool(int(buff[0]))
    b = bool(int(buff[1]))
    c = bool(int(buff[2]))
    d = bool(int(buff[3]))
    e = bool(int(buff[4]))
    f = bool(int(buff[5]))
    g = bool(int(buff[6]))
    h = bool(int(buff[7]))

    U1 = a and not c
    U2 = not c and not b
    U3 = a and b
    U4 = U1 and not d
    U5 = U2 and not d
    U6 = U3 and not d
    U7 = not f and c
    U9 = U4 and not e
    U10 = U5 and not e
    U11 = U6 and not e
    U18 = f ^ g
    U12 = U7 and U18
    U19 = (not h) ^ (not b)
    U8 = U19 and c
    U21 = U9 or U10
    U22 = U11 or U12
    U23 = U22 or U8
    U24 = U21 or U23

    return str(int(U24))

with open("key.txt", 'r') as keyFile:
    key = keyFile.readline()

key = key.strip('\n')

clear_key = ""
buff = ""
for char in key:
    buff += char

    if buff.__len__() == 8:
        clear_key += decode(buff)
        buff = ""

print(clear_key)

human_key = ""
buff = ""
for char in clear_key:
    buff += char

    if buff.__len__() == 8:
        print(buff, int(buff, 2), chr(int(buff, 2)))
        human_key += chr(int(buff, 2))
        buff = ""

print(human_key)
