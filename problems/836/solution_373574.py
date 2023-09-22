def busca(setor,matriz):
    pessoa = []
    for i in range(0,2):
        if matriz[i][2] == setor:
            pessoa += matriz[i]
    return pessoa