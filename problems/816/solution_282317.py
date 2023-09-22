def maiores(lista_numeros, n):
    lista_numeros.append(n)
    lista_numeros.sort()
    index = lista_numeros.index(n)
    del lista_numeros[:index]
    return lista_numeros