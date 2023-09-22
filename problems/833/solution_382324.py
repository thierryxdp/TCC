def conta_numero(numero,matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(linha):
        lista = []
        for j in range(linha):
            pos = matriz[i][j]
            if pos==numero:
                lista.append(pos)
    return lista