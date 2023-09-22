def maiores(lista, n):
    
    lista.append(n)
    lista.sort()
    index = lista.index(n)
    return lista[index+1:]