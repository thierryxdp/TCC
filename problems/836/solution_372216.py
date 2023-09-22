def busca(c,matriz):
    for i in range(len(matriz)+1):
        if c in matriz[i]:
            lista=matriz[i].remove(c)
            return [matriz[i]]