def busca(setor,matriz):
    """A função retorna dados de todos os funcionários de um determinado
    setor.
    str-->list"""
    lista1 = []
    for lista in range(len(matriz)):
        for item in range(len(lista)):
            if matriz[0][2] == setor:
                lista1.append(matriz[0][2])
    for x in range(len(lista1)):
        if dados[x][2] == setor:
            del remove[y][2]
    return lista1