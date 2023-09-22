def filtra_pares(x1,x2,x3,x4): 

    tupla = (x1, x2, x3, x4)
    n1 = int(tupla[0])
    n2 = int(tupla[1])
    n3 = int(tupla[2])
    n4 = int(tupla[3])
             
    elemPares = '' 

    if n1 % 2 == 0:
        elemPares = n1

    elif n2 % 2 == 0:
        elemPares = n2

    elif n3 % 2 == 0:
        elemPares = n3

    elif n4 % 2 == 0:
        elemPares = n4

    return elemPares