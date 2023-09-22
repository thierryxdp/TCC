def busca(buscar,matriz):
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if buscar == matriz[l][c]:
                del(matriz[l][c])
                return [matriz[l]