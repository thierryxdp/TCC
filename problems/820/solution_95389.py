def posLetra(frase,letra,posicao):
    i = frase.find(letra)
    if posicao == 1:
        return i
    elif posicao > 1:
        return frase.find(letra, posicao)