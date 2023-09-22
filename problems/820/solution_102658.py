def posLetra(string,letra,numero):
    '''Uma função que indica a posição desejada de uma determinada letra,
    em sua ocorrencia n. Caso exista menos ocorrencias da letra do que a ocorrencia
    pedida, a funcao retornara -1.
    str +str +int -> int'''
    posicao = 0
    encontrados = 0
    atual = ''
    if n > str.count(string, 1):
        return -1
    while posicao < len(string) and encontrados < n:
        atual = string [posicao]
        if atual == 1:
            encontrados += 1
        posicao += 1
    if encontrados == n:
        return posicao -1