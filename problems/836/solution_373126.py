def busca(setor,matriz):
    funcionarios = []
    for i in matriz:
        for j in i:
            if j == setor:
                list.remove(i,j)
                list.append(funcionarios, i)
    return funcionarios