def posLetra(frase,letra,posicao):
    f = len(frase)
    i = frase.find(letra)
    if posicao > 0:
        return frase.find(letra, posicao)