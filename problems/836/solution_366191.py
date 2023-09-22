def busca(informacao, matriz):
    setor = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])) and matriz[i][j] != informacao:
            if str.count(informacao,matriz[i][j])>0:
                setor += matriz[i],
    return setor