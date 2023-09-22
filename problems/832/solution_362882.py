def eh_quadrada(matriz):
    linha = len(matriz)
    respotacerta = ''
    for elemento in matriz:
    coluna = len(matriz[0])
        if linha == coluna:
            respostacerta = True
        elif linha != coluna:
            respostacerta = False
        elif linha or coluna == []:
            respostacerta = True
    return respostacerta