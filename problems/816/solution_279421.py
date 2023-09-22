def maiores(lista_de_numeros, n):
    lista_resultado = []
    for numero in lista_de_numeros:
        if numero > n:
            lista_resultado.append(numero)
    return lista_resultado