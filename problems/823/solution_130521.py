def faltante(lista):
    
    lista1 = lista[:]
    n = len(lista1)
    list.sort(lista1)
    
    lista2 = list(range(1, n + 1))
    i = 0
    
    while lista1[i + 1] - lista1[i] == 1 and i < n - 1:
        i += 1
    
    return i + 1