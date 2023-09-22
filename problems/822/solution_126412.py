def repetidos(lista_numeros):
    lista = ()
    i = 1
    while i<len(lista_numeros):
        if lista_numeros[i] != lista_numeros[i-1]:
            lista = lista + (0,)
        if lista_numeros[i] == lista_numeros[i-1]:
            lista = lista + (1,)
        i = i + 1
    return sum(lista)