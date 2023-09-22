def posLetra(frase,letra,numero):
    i = 0
    posicao = 0
    while i < len(frase):
        if frase[i] == letra:
            posicao += i
        elif posicao == numero:
            posicao += 1
        i += 1
        return