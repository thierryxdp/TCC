def repetidos (lista):
    '''Diz o número de vezes que numeros estão
    repetidos em uma lista númerica;
    list -> int'''
    repeticoes = 0
    posicao = 0
    while posicao < len(lista):

        if lista[posicao - 1] == lista[posicao]:
            repeticoes = repeticoes + 1
            posicao = posicao + 1

        else:
            posicao = posicao + 1

    return repeticoes