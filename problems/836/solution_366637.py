def busca(string,matriz):
    retorna=[]
    for i in range(len(matriz)):
        if string==matriz[i][2]:
            nova=matriz[i]
            retorna.append(nova.remove(string))
    return retorna