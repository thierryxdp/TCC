def busca(c,matriz):
    for i in range(len(matriz)):
        if c in matriz[i]:
            lista=matriz[i].remove(c)
            return [matriz[i]]
        else:
            return []