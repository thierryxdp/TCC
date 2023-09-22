def filtra_pares(a,b,c,d):
    lista1 = [a,b,c,d]
    lista2 = filter(x % 2 == 0,lista1) 
    return list(lista2)