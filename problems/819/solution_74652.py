def filtraMultiplos(lista,n):
    lista1=[]
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n==0:
            lista1 = lista1 + lista[proximo]
            proximo = proximo + 1
    return lista1