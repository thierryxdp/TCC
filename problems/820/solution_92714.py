def posLetra(string,letra,numero):

    contador = 0
    posicoes = []


    while contador < len(string):
        if string[contador] == letra:
            list.append(posicoes, contador)
        contador += 1

    if numero > string.count(letra):
        return -1

    return posicoes[numero-1]