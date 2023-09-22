def posLetra(texto,letra,numero):
    posicao = 0
    repeticao= 0
    for item in texto:
        if item == letra:
            repeticao+=1
        if numero == repeticao:
            break
        posicao+=1
    if repeticao != numero:
        return -1
    return posicao