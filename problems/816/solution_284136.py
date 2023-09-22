def maiores(lista, n):
    lista = lista + [n]
    list.sort(lista)
    if n < lista[1]:
        return lista[1:]
    
    elif n < lista[0]:
        return lista[:]
    
    elif n < lista[2]:
        return lista[2:]
    
    elif n < lista[3]:
        return lista[3:]