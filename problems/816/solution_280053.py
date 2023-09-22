def maiores(lista_numeros, n):
    for i in lista_numeros:
        if i < n:
            lista_numeros.remove(lista_numeros[i])

    lista_numeros.sort()
    return lista_numeros