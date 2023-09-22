def filtra_pares(t): 

    n1 = int(t[0])
    n2 = int(t[1])
    n3 = int(t[2])
    n4 = int(t[3])
             
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