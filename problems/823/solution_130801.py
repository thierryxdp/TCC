def faltante(lista):
    
    lista.sort()
    
    list1 = range(lista[0], lista[-1])
    list2 = range(lista[0], len(lista))
    
    list1 = set(list1)
    list2 = set(list2)
    
    x = list1.difference(lista2)
    
    return x