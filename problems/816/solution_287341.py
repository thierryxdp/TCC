def maiores(lista_numeros, n):
    i = 0
    list_atualizada = []
    while i < len(lista_numeros):
        if list_numeros[i] > n:
        list_atualizada.append(lista_numeros[i])
        i += 1
    list_atualizada.sort()
    return list_atualizada