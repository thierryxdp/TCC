def busca(string,matriz):
    retorna=[]
    for i in range(len(matriz)):
        if string==matriz[i][2]:
            nova=matriz[i].copy()
            retorna.append(nova)
    return nova