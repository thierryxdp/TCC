def busca(setor, matriz):
    funcionarios = []
    for i in range(len(matriz)):
        if str.find((matriz[i][2]).lower(), setor.lower()) != -1:
            funcionarios.append(matriz[i])
    return funcionarios