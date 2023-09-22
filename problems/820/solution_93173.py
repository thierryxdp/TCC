def posLetra(frase,letra,ocorrencia):
    I=frase.count(letra)
    if I<ocorrencia:
        return -1
    while I<ocorrencia:
        A=frase.index(letra)+I
    I=I+1
    return frase