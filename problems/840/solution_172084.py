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
        return x-1
    elif y != 0 and y<x and y<z:
        return y-1
    elif z != 0 and z<x and z<y:
        return z-1