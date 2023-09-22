def maiores(lista, n):
    
    lista.sort()

    if n in lista:
        index = lista.index(n)
        return lista[index:]
    return lista