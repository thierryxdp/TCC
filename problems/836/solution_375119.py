def busca(pesquisa,matriz):
    result=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if pesquisa in matriz[i]:
                matriz[i].remove(pesquisa)
                result=matriz[i]
    return result