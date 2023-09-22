def busca(buscar,matriz):
    resposta = []
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if buscar == matriz[l][c]:
                del(matriz[l][c])
                resposta = matriz[l]
    return resposta