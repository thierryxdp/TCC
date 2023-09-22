def busca(c,matriz):
    for i in range(len(matriz)):
        i=i+1
        if c in matriz[i]:
            lista=matriz[i].remove(c)
            return [matriz[i]]