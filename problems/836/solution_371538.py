def busca(setor,matriz):
    func = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == setor:
                func = func + [matriz[i]]
    return func