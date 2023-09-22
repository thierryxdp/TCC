def posLetra(frase,letra,numero):
    i = 0
    posicao = 0
    while i < len(frase):
        if frase[i] == letra:
            posicao += 1
        if posicao == numero:
                return i
        i += 1
        return -1