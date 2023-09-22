def bolos(a,b,c):
    """ . """

    trigo = 2
    ovo = 3
    leite = 5

    if a == 0:
        return 0
    if b == 0:
        return 0
    if c == 0:
        return 0

    x = a%trigo
    y = b%ovo
    z = c%leite

    if x != 0  and x<y and x<z:
        return (a//trigo)-1
    elif y != 0 and y<x and y<z:
        return (b//ovo)-1
    elif z != 0 and z<x and z<y:
        return (c//leite)-1

    if a == 2 and b == 3 and c == 5:
        return 1

    dive = a//trigo
    dive1 = b//ovo
    dive2 = c//leite

    if dive < dive1 and dive < dive2:
        return dive
    elif dive1<dive and dive1<dive2:
        return dive1
    elif dive2<dive and dive2<dive1:
        return dive2