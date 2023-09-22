def busca(c,matriz):
    for i in range(len(matriz)):
        if c in matriz[i]:
            lista=matriz[i].remove(c)
            return [matriz[i]]
        elif c in matriz[i+1]:
            lista=matriz[i+1].remove(c)
            return [matriz[i]+matriz[i+1]]