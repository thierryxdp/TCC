def posLetra(texto,letra,numero):
    i = 0
    posicao = 0
    while i < len(texto):
        if texto[i] == letra:
            i += 1
            if posicao == numero:
                return i
        i += 1
    return -1