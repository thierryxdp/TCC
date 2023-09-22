def posLetra(string, palavra, ocorrencia):
    '''Dada uma string retorna o indice da ocrrencia de uma letra
    str, str, int -> int'''
    if ocorrencia > string.count(palavra):
        return -1
    j = 0
    z = 1
    h = []
    h[:] = string
    while z < ocorrencia:
        if h[j] == palavra:
            z += 1
        j += 1
    return j - 1