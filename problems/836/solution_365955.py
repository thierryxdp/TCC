def busca(setor, matriz):
    funcionarios = []
    for x in range(len(matriz)):
        if setor in matriz[x][2]:
            list.append(funcionarios, matriz[x])
    return funcionarios