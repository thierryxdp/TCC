def posLetra(frase,letra,ocorrencia):
    if str.count(frase,ocorrencia)!=0:
        return str.index(frase,letra)
    else:
        return '-1'