def maiores(lista_de_numeros, n):
    lista_resultado = []
    for numero in lista_de_numeros:
        if numero > n:
            lista_resultado.append(numero)
    lista_resultado.sort()
    return lista_resultado