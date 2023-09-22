def busca(setor, matriz):
    pessoas_setor = []
    for l in range(len(matriz)):
        for d in range(len(matriz[0])):
            if matriz[l][d] == setor:
                pessoas_setor.append(matriz[d])
    return pessoas_setor