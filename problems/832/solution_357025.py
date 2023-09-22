def eh_quadrada(matriz):
    for i in range(len(matriz)):
        coluna = range(len(matriz[0]))
        if i == coluna[i]:
            return True
        else:
            return False