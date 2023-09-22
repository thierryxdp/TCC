def busca(setor, matriz):
    """retorna os dados de todos os funcionários a partir
    de uma matriz
    List => list"""
    achados = []
    for i in range(len(matriz)):
        if (matriz[i][2] == setor):
            achados.append(matriz[i][0:2] + matriz[i][3:4])

    return achados