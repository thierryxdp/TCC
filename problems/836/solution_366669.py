def busca(funcao, matriz):
    funcionarios = []
    for dados in range(len(matriz)):
        if matriz[dados][2] == funcao:
            list.remove(matriz[dados], funcao)
            list.append(funcionarios, matriz[dados])
    return funcionarios