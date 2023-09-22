def filtraMultiplos(lista,n):
    lista_nova = []
    proximo = 0
    while proximo<len(lista):
        if lista[proximo]%n==0:
             lista_nova = lista_nova + [lista[proximo]]
        proximo = proximo + 1
    return lista_nova