def filtra_pares(elem):
     
        pares= ( )
    if elem[0] % 2 == 0:
        pares = pares + (elem[0],)
    if elem[1] % 2 == 0:
        pares = pares + (elem[1],)
    if elem[2] % 2 == 0:
        pares = pares + (elem[2],)
    if elem[3] % 2 == 0:
        pares = pares + (elem[3],) 
        return pares