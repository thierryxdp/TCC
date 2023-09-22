def posLetra(frase,letra,posicao)
    if posicao*letra in frase:
     return str.find(frase,letra,posicao - 1)
    else:
        return -1