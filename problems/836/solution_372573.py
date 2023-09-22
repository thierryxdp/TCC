def busca(setor, matriz):
    funcionarios = []
    funcionario = []
    for x, y in enumerate(matriz):
        if matriz[x][2] == setor:
            funcionario = [z for z in matriz[x] if z != setor]
            if funcionario != []:
                funcionarios = funcionarios.append(funcionario)
    return funcionarios