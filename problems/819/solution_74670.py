def filtraMultiplos(lista,n):
    lista[0]
    lista1 = ()
    proximo = 0
    while proximo < len(lista[0]):
        if lista[0][proximo] %n == 0:
            lista1 = lista1 + (lista[0][proximo],)
            proximo = proximo + 1
    return lista1