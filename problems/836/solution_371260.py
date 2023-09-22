def busca(matriz, setor):
    funcionarios = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            funcionarios.append(matriz[i])
    return funcionarios