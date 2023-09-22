def posLetra(string, letra, numero):
    contador = 0
    posicao = 0
    while contador != numero:
        posicao = str.index(string, letra, posicao+1, len(string))
        contador = contador + 1
    return posicao