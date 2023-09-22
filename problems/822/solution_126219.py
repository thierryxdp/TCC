def repetidos(lista_numeros):
    '''
        recebe uma lista de numeros e retorna o numero de vezes em que um
        de seus elementos aparece repetido nessa lista
        entrada: lista
        saida: inteiro
    '''
    chq = 1
    ocorrencia = 0
    while chq < len(lista_numeros):
        if lista_numeros[chq] == lista_numeros[chq-1]:
            ocorrencia = ocorrencia + 1
        chq = chq + 1
    return ocorrencia