def posLetra(frase,letra,posicao):
    ocorrencia=str.index(frase,letra)
    nfrase=str.replace(frase,letra,'substitui1'posicao-1)
    if posicao<=ocorrencia:
        return str.find(nfrase,letra)
    else:
        return -1