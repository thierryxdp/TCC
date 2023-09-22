def posLetra(frase,letra,ocorrencia):
    if str.count(frase,letra)!=0:
        return str.index(frase,letra)
    else:
        return '-1'