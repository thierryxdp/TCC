def posLetra(frase,letra,posicao):
    if posicao*letra in frase:
     return str.find(frase,letra,posicao)
    else:
        return -1