def busca(informacao, matriz):
    pos = 0
    setor = []
    linha_x = matriz[pos]
    for pos in range(len(matriz)):
        for pos in range(len(linha_x)):
            if informacao in linha_x == True:
                setor += linha_x
    return setor