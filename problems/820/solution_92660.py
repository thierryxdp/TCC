def posLetra (string, letra, ocorrencia):
    '''retorna a posicao da string em que a ocorrencia desejada da letra inserida se encontra
    str, str, int -> int'''
    i = 0
    n = 0
    while string[i] != letra and n != ocorrencia:
        if string[i] = letra:
            n = n + 1
        i = i + 1
    return i