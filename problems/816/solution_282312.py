def maiores(lista_numeros, n):
    lista_numeros.sort()
    del lista_numeros[0:n]
    return lista_numeros