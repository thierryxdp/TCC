def conta_numero(numero,matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(coluna*linha):
        lista = []
        for j in range(coluna*linha):
            if matriz[i][j] in numero:
                lista.append(matriz[i][j])
    return lista