def busca(setor, matriz):
    pessoas_setor = []
    for l in range(len(matriz)):
        for d in matriz[l][2]:
            if setor == matriz[l][d]:
                pessoas_setor.append(matriz[d])
    return pessoas_setor