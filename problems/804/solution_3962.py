def filtra_pares(t): 

    n1, n2, n3, n4 = int(t[0:5])
             
    elemPares = () 

    if n1 % 2 == 0:
        elemPares = n1

    elif n2 % 2 == 0:
        elemPares = n2

    elif n3 % 2 == 0:
        elemPares = n3

    elif n4 % 2 == 0:
        elemPares = n4

    return elemPares