def filtra_pares(tup):
    return tup%2
    conj = [1,2,3,4]
    filtro = filter(filtra_pares,conj)
    
    print(list(filtro))