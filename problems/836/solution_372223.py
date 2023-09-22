def busca(c,matriz):
    h=len(matriz)
    for i in range(h):
        for j in range(h):
            if c in matriz[i]:
                lista=matriz[i].remove(c)
                return [matriz[i]]