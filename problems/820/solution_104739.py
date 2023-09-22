def posLetra(frase,letra,numero):
    i = 0
    posicao = 0
    while i < len(frase):
        if frase[i] == letra:
            posicao += 1
        elif posicao == numero:
            return i
        i += 1
        else:
            -1