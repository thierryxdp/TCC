def maiores(lista, n):
    lista.append(n)
    lista.sort()
    lista=lista[lista.index(n):-2]
    
    return lista