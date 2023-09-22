def posLetra(frase,letra,ocorrencia):
    i = 0
    n = 0
    while i<len(frase) and n<ocorrencia:
        if frase[i] == letra:
            n = n +1
        i = i + 1
    if n < ocorrencia:
        return -1
    else:
        return i-1