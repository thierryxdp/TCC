def maiores(lista, n):
    lista.append(n)
    lista.sort()
    lista=lista[n+1:]
    
    return lista