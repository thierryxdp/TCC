def busca(matriz,setor):
    funcionarios = []
    c = 0
    for i in matriz:
        if i[2] == setor:
            del(i[2])
            funcionarios.append(i)
            c += 1
    return funcionarios