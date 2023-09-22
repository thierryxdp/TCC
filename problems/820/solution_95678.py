def posLetra(frase,letra,posicao):
    ocorrencia=str.count(frase,letra)
    nfrase=str.replace(frase,letra,'@',posicao-1)
    if posicao<=ocorrencia:
        return str.find(nfrase,letra)
    else:
        return -1