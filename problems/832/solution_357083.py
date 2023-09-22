def eh_quadrada(matriz):
    linha = 0
    coluna = 0
    for i in range(len(matriz)):
        linha = linha + 1
        for j in range(len(matriz[i])):
            coluna = coluna + 1
    if linha == coluna:
        return True
    elif linha =! coluna:
        return False