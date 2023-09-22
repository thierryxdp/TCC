def posLetra(frase, x, n):
"""
str, str, int -> int
"""
    ocorrencia  = 0
    for i in range(len(frase)):
        h = frase[i]
        if h == x:
            ocorrencia  = ocorrencia  + 1
        if ocorrencia == n:
            return i
    return -1