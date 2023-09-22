def posLetra(texto, letra, ocorrencia):
    ''' Essa função recebe uma string, uma letra e um numero que indica a ocorrencia
    desejada da letra. A função retorna em que posição da string aquela ocorrencia está
    str, str, int -> int'''
    i = 0
    n = 0
    while i<len(texto) and n<ocorrencia:
        if texto[i] == letra:
            n = n +1
        i = i + 1
    if n < ocorrencia:
        return -1
    else:
        return i-1