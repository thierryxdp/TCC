def repetidos(lista):
    '''
       Função que recebe uma lista de numeros e retorna
       quantas vezes tal numero apareceu repetido
       list -> int
    '''
    L = 0
    quant_vezes = 0

    while len(lista) > L:
        if lista[L] == lista[L - 1]:
            quant_vezes = quant_vezes + 1
            L = L + 1
        else:
            L = L + 1

    return quant_vezes