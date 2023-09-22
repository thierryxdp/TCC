def posLetra(frase,letra,ocorrencia):
    i = 0
    n = 0
    while i<len(frase) and n<ocorrencia:
        if frase[i] == letra:
            nocs = nocs +1
        i = i + 1
    if nocs < ocorrencia:
        return "so foram encontradas "+str(nocs)+" ocorrencias de "+str(letra)
    else:
        return i-1