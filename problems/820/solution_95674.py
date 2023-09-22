def posLetra(frase,letra,posicao):
    ocorrencia=str.index(frase,palavra)
    nfrase=str.replace(frase,letra,posicao-1)
    if posicao<=ocorrencia:
        return str.find(nfrase,palavra)
    else:
        return -1