def busca(setor, matriz):
    func = []
    for funcionario in matriz:
        if setor == funcionario[2]:
            encontrado = funcionario[:]
            del encontrado[2]
            func.append(encontrado)
    return func