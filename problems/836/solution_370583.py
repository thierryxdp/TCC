def busca(setor,matriz):
    funcionarios = []
    c = 0
    for i in matriz:
        if setor == i[2]:
            del(i[2])
            funcionarios.append(i)
            c += 1
    return funcionarios