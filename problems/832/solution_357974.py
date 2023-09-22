def eh_quadrada(matriz):
    quantidadeElementos = len(matriz)
    matrizNova = []
    for l in range(0,quantidadeElementos):
        for c in range(0,quantidadeElementos):
            matrizNova[l][c] = matriz
    if quantidadeElementos / len(matrizNova) == 0:
        return True
    else:
        return False