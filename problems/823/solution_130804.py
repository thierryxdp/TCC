def faltante(lista):
    
    lista.sort()
    
    list1 = range(lista[0], lista[-1])
    
    list1 = set(list1)
    
    x = list1.difference(lista)
    
    return int(x)