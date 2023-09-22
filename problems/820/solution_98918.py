def posLetra(string,letra, n):
    '''
    funcao retorna a posicao da string em que a ocorrência está
    '''
    h = string.find(letra)
    while h >= 0 and n > 1:
        h = string.find(letra, h + 1)
        n =n- 1
    return h