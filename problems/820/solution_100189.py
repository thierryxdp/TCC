def posLetra(frase,letra,ocorrencia):
    i=0
    while str.index(frase,letra) != ocorrencia:
        if letra in frase:
            return str.index(frase,letra)
        else:
            return -1
        i=i+1