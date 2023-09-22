def posLetra(string,letra,ocorrencia):
    '''Funcao que retorna em que posicao da string aquela ocorrencia da letra
    recebida esta
    str, str, int -> int'''
    pos = string.find(letra)
    while pos >= 0 and ocorrencia > 1:
        pos = string.find(letra, pos + 1)
        ocorrencia = ocorrencia - 1
    return pos