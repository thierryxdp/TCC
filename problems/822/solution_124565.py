def repetidos(lista_de_numeros):
    i = 0
    while i < len(lista_de_numeros):
        if list.count(lista_de_numeros, lista_de_numeros[i]) <= 1:
            del lista_de_numeros[i]
        if list.count(lista_de_numeros, lista_de_numeros[i]) == 1:
            del lista_de_numeros[i]
        if list.count(lista_de_numeros, lista_de_numeros[i]) >= 2:
            del lista_de_numeros[i]
        i += 1
    return len(lista_de_numeros)