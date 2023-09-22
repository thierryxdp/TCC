def repetidos(listaNumeros):
    '''funçao que dada uma lista de numeros e retorna o numero de vezes que um elemento da lista é igual ao anterior:list->int'''
    i = 0
    vezesRepetidos = 0
    while (i < len(listaNumeros)-1):
        if (listaNumeros[i+1] == listaNumeros[i]):
            vezesRepetidas += 1:
        i += 1
    return vezesRepetidas