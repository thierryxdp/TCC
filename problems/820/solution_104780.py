def posLetra (string, letra, n_ocorrencia):
    '''Função que retorna a posição da ocorrência de uma
    determinada letra em uma string
    str, str, int -> int'''
    
    posicao = texto.find(letra)
    while posicao >= 0 and n_ocorrencia > 1:
        posicao = texto.find(n_ocorrencia, posicao + 1)
        n = -1
    return posicao