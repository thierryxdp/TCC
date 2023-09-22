def posLetra(frase, letra, numero):
    i = 0
    while i < len(frase):
        if frase.index(letra) == numero:
            i += 1
        elif frase.index(letra) != numero:
        return -1
    return i