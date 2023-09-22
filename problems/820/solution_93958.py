def posLetra(string, letra, numero):
    i = 0
    posicao = 0
    while i <= len(string):
        posicao = string.index(letra) * numero
        
        i += 1

    return posicao