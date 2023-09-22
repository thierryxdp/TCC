def posLetra (string, letra, n_ocorrencia):
    '''Função que retorna a posição da ocorrência de uma
    determinada letra em uma string
    str, str, int -> int'''
    posicao = string.find(letra)
    menos_ocorrencias = -1
    
    while posicao >= 0 and n_ocorrencia > 1:
        n_ocorrencia = -1
    return posicao or menos_ocorrencias