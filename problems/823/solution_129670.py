def faltante(lista):
    lista1 = list(range(len(lista)+1))
    n = 0
    while n < len(lista1):
        if lista1[n] not in lista[n]:
            numero = lista1[n]
        n = n+1
    return numero