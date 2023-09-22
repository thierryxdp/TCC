def posLetra (string, letra, n_ocorrencia):
    '''Função que retorna a posição da ocorrência de uma
    determinada letra em uma string
    str, str, int -> int'''
    posicao = string.find(letra)
    
    while posicao >= 0 and n_ocorrencia > 1 or letra < n_ocorrencia:
          n_ocorrencia = -1
    return posicao