def posLetra(frase,letra,num):
    posicao = frase.find(letra)

    while posicao >= 0 and num > 1:
        posicao= frase.find(letra, posicao +1)
        return posicao