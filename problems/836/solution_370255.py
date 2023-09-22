def busca(setor, matriz):
    funcionarios = []
    for i in range(len(matriz)):
        if str.find((matriz[i][2]).lower(), setor.lower()) != -1:
            funcionarios = funcionarios + [matriz[i][:2] + matriz[i][3:]]
    return funcionarios