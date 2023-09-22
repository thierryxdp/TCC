def busca(setor, matriz):
    funcionarios = []
    for i in range(0, len(matriz) - 1):
        if str.find((funcionarios[i][2]).lower(), setor.lower()) != -1:
            funcionarios.append(matriz[i])
    return funcionarios