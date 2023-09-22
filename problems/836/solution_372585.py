def busca(setor,m):
    funcionarios = []
    for i in range(len(m)):
        if m[i][2] == setor:
            list.append(funcionarios,m[i])
            list.remove(funcionarios[i],setor)
    return funcionarios