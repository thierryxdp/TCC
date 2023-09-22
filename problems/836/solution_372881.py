def busca(setor,matriz):
    """busca em uma matriz e retorna uma lista de acordo com a busca"""
    busca=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            a=matriz[i]
            resposta=list.remove(a,setor)
            list.append(busca,resposta)
    return busca