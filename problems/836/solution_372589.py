def busca(setor,m):
    funcionarios = []
    for i in range(len(m)):
        if m[i][2] == setor:
            list.append(funcionarios,m[i])
            del funcionarios[list.index(funcionarios,m[i])][2]
    return funcionarios