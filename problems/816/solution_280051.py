def maiores(lista_numeros, n):
    i = 0
    while i <= len(lista_numeros):
        if lista_numeros[i] < n:
            lista_numeros.remove(lista_numeros[i])
        i += 1

    lista_numeros.sort()
    return lista_numeros