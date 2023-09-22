def filtra_pares(t): 

    n1, n2, n3, n4 = t
    
    elemPares
    elemPares2
    elemPares3
    elemPares4

    if n1 % 2 == 0:
        elemPares = n1

    elif n2 % 2 == 0:
        elemPares2 = n2 + elemPares[0:]

    elif n3 % 2 == 0:
        elemPares3 = n3 + elemPares2[0:]

    elif n4 % 2 == 0:
        elemPares4 = n4 + elemPares3[0:]

    return elemPares4