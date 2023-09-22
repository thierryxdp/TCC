def filtra_pares(x1,x2,x3,x4): 

    tupla = (x1, x2, x3, x4)
    elemPares = '' 

    if tupla[:1] % 2 == 0:
        elemPares = tupla[:1]

    elif tupla[1:2] % 2 == 0:
        elemPares = tupla[1:2]

    elif tupla[2:3] % 2 == 0:
        elemPares = tupla[2:3]

    elif tupla[3:4] % 2 == 0:
        elemPares = tupla[3:4]

    return elemPares