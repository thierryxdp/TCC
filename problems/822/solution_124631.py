def repetidos(listaNumeros):
    '''funçao que dada uma lista de numeros e retorna o numero de vezes que um elemento da lista é igual ao anterior:list->int'''
    i = 1 - len(listaNumeros)
    vezesRepetidos = 0
    while i <= len(listaNumeros):
        if (listaNumeros[i] == listaNumeros[1-i]):
            vezesRepetidas += 1
    return vezesRepetidas