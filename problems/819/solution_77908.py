def filtraMultiplos(lista1,n):
    lista2 = []
    proximo = 0
    while proximo<len(lista1):
        if lista1[proximo]%n == 0:
            lista2 = lista2 + [lista1[proximo]]
    proximo = proximo + 1 
    return lista2