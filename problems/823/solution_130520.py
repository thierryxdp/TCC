def faltante(lista):
    
    lista1 = lista[:]
    n = len(lista1)
    lista2 = list(range(1, n + 1))
    list.sort(lista1)
    i = 1
    
    while ((lista1[i] == lista2[i]) or (i < n)):
        i += 1
    
    return i