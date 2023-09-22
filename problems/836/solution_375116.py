def busca(pesquisa,matriz):
    result=[]
    for i in range(len(matriz)):
        for pesquisa in matriz[i]:
            matriz[i].remove(pesquisa)
            result=matriz[i]
    return result