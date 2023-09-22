def eh_quadrada(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    respotacerta = ''
    for elemento in matriz:
        if linha == coluna:
            respostacerta = True
        elif linha != coluna:
            respostacerta = False
    return respostacerta