def posLetra(frase,letra,ocorrencia):
    """Função que retorna a posição da ocorrência da letra na frase. Caso existam menos ocorrências do que a ocorrência dada como entrada, a função retorna -1
str, str, int -> int"""

    posicao = frase.find(letra)

    while posicao >= 0 and ocorrencia > 1:
        posicao = frase.find(letra, posicao + 1)
        ocorrencia = ocorrencia - 1
    return posicao