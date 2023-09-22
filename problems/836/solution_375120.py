def busca(pesquisa,matriz):
    result=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if pesquisa==matriz[i][j]:
                matriz[i].remove(pesquisa)
                result=matriz[i]
    return result