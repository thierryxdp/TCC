def maiores(lista, n):
    
    lista.sort()
    index = lista.index(n)
    return lista[index:]