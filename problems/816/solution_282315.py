def maiores(lista_numeros, n):
    lista_numeros.append(n)
    lista_numeros.sort()
    del lista_numeros[:n]
    return lista_numeros