def maiores(lista_numeros, n):
    i = 0
    lista_atualizada = []
    while i < len(lista_numeros):
        if lista_numeros[i] > n:
         lista_atualizada.append(lista_numeros[i])
        i += 1
    return lista_atualizada