def busca(c,matriz):
    h=len(matriz)
    for i in range(h):
        for j in range(h):
            if matriz[i][2]==c:
                lista=matriz[i].remove(c)
                matriz=matriz[i]
    return [matriz]