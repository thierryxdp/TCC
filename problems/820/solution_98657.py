def posLetra(f, l, o):
    '''Retorna a posição da letra(l) na frase(f) na ocorrência(o).
    Caso não encontre retorna -1.
    str, str, int -> int'''
    i = 0
    ocorrencia = 0
    while i < len(f):
        if f[i] == l:
            ocorrencia += 1
        if ocorrencia == o:
            return i
        i += 1
    return -1