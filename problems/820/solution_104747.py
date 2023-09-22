def posLetra(frase,letra,numero):
    i = 0
    posicao = 0
    while i < len(frase):
        if frase[i] == letra:
            return i
        elif posicao == numero:
            return i
        i += 1
        return posicao