def eh_quadrada(matriz):
    linha = len(matriz)
    respotacerta = ''
    if matriz == []:
        respostacerta = True
    coluna = len(matriz[0])
    for elemento in matriz:
        if linha == coluna:
            respostacerta = True
        elif linha != coluna:
            respostacerta = False
        elif linha and coluna not in matriz:
            respostacerta = True
    return respostacerta