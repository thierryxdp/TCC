def posLetra(frase,letra,ocorrencia):
    if str.count(frase,letra)>=ocorrencia:
        while str.count(frase,letra)==1:
        return str.index(frase,letra)
    else:
        return -1