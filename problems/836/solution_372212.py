def busca(c,matriz):
    for i in range(len(matriz)):
        if c in matriz[i]:
            i=i+1
            lista=matriz[i].remove(c)
            return [matriz[i]]