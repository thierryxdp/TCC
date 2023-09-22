def posLetra(frase,procura,ocorrencia):
    if ocorrencia>=1:
        return str.index(frase,procura,ocorrencia)
    else:
        return -1