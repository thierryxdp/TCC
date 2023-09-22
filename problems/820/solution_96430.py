def posLetra(frase,procura,ocorrencia):
    x=str.index(frase,procura,ocorrencia)
    if ocorrencia<=x:
        return x
    else:
        return -1