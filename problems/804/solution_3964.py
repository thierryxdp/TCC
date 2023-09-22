def filtra_pares(t): 

    n1, n2, n3, n4 = t 

    if n1 % 2 == 0:
        x1 = n1

    elif n2 % 2 == 0:
        x2 = n2

    elif n3 % 2 == 0:
        x3 = n3

    elif n4 % 2 == 0:
        x4 = n4
        
    elemPares = x1, x2, x3, x4

    return elemPares