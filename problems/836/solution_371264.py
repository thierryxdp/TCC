def busca(setor, matriz ):
    funcionarios = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            funcionarios.append([matriz[i][0],matriz[i][1],matriz[i][3]])
    return funcionarios