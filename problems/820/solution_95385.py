def posLetra(frase,letra,posicao):
    f = len(frase)
    i = frase.find(letra)
    if posicao > 1:
        return frase.find(letra, posicao)