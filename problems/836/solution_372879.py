def busca(setor,matriz):
    """busca em uma matriz e retorna uma lista de acordo com a busca"""
    busca=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            list.append(busca,list.remove(matriz[i],setor))
    return busca