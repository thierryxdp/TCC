def eh_quadrada(matriz):
    linha = len(matriz)
    coluna = len(matriz[])
    respotacerta = ''
    for elemento in matriz:
        if linha == coluna:
            respostacerta = True
        elif linha != coluna:
            respostacerta = False
        elif linha or coluna == []:
            respostacerta = True
    return respostacerta