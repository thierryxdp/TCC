def maiores(lista_numeros, n):
    lista_final = []
    for numero in lista_numeros:
        if numero > n:
            lista_final.append(numero)
    return lista_final