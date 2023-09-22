def posLetra(texto, letra, ocorrencia):
    ''' Funcao que retorna a ocorrencia de onde a letra esta
str, str, int -> int'''
    total = texto.count(letra)
    ocorrencia = int(ocorrencia)
    if (0< ocorrencia <= total):
        posicao = -1
        while (ocorrencia >0):
            posicao = texto.index(letra, posicao +1)
            ocorrencia = ocorrencia - 1
        return posicao
    else:
        return -1