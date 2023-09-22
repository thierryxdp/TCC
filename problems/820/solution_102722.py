def posLetra(frase,letra,ocorrencia):
    i = 0
    n = 0
    while i<len(frase) and n<ocorrencia:
        if frase[i] == letra:
            nocs = n +1
        i = i + 1
    if nocs < ocorrencia:
        return str(n)+str(letra)
    else:
        return i-1