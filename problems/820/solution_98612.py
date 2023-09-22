def posLetra(string,letra,numero):
    ''' Função que dados uma string, uma letra e um número que
    indica a ocorrência específica da letra na string, retorna
    a posição da string em que tal ocorrência está inserida.
    Retorna -1 caso ocorra menos ocorrências da letra que a pedida.
    Entrada: str, str, int
    Retorno: int '''

    posicao = []
    indice = 0
    
    while indice < len(string):
        if letra in string[indice]:
            list.append(posicao,indice)
        indice += 1

    if numero <= len(posicao):
        return posicao[numero-1]
    else:
        return -1