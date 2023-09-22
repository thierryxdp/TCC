def maiores(lista, n):
    
    if n in lista:
        lista.sort()
        index = lista.index(n)
        return lista[index:]
    return lista