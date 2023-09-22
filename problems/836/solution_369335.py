def busca(setor,matriz):
    """Função que dado um setor da empresa, retorna dados de todos os funcionarios do respectivo setor.
    list(list),str - > list(tuple)"""
    lista = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            list.remove(matriz[i], matriz[i][2])
            lista.append(matriz[i])
    return lista