def posLetra (string, letra, n):
    '''Retorna a posição da letra dada
    na enésima (n) vez em que aparece
    na string inserida
    str, str, int --> int'''
    i = 0
    ocorrencia = -1
    if str.count(string, letra) < n:
        return -1
    while i < n:
        ocorrencia = str.index(string, letra, ocorrencia+1)
        i += 1
    return ocorrencia