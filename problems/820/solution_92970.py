def posLetra(string, letra, numOcorrencia):
    '''Recebe uma string, uma letra e o número da ocorrência desejada da
    letra (1 para a primeira, 2 para a segunga, etc.) e retorna a posição
    da string em que aquela ocorrência está.
    Se existir menos ocorrências dessa letra do que a ocorrencia pedida,
    retorna -1.
    
    str, str, int -> int'''

    if str.count(string, letra) < numOcorrencia:
        return -1

    ocorrenciaLetra = 0
    posicao = -1

    while ocorrenciaLetra != numOcorrencia:
        posicao = posicao + 1
        if string[posicao] == letra:
            ocorrenciaLetra = ocorrenciaLetra + 1

    return posicao