def busca(setor,matriz):
    """Recebe uma matriz de 4 linhas por coluna e um setor e retorna os dados de cada funcionário do setor/str,list->list"""
    lista=list()
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            lista.append(matriz[i])
        for i in range(len(lista)):
            del(lista[i][2])
    return lista