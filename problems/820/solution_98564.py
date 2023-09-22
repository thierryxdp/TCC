def posLetra(string, letra, numero):
    contador = 0
    posicao = 0
    while contador != numero:
        posicao = str.find(string, letra, posicao, len(string))
        contador = contador + 1
    return posicao