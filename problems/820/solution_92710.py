def posLetra(string,letra,numero):

    contador = 0
    posicoes = []


    while contador < len(string):
        if string[contador] == letra:
            list.append(posicoes, string[contador])
        contador += 1

    if string[contador] not in letra:
        return -1

    return posicoes[numero-1]