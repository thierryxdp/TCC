def busca(setor, matriz ):
    funcionarios = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            funcionarios.append(matriz[i])
    return funcionarios