def busca(setor,matriz):
    """A função retorna dados de todos os funcionários de um determinado
    setor.
    str-->list"""
    lista1 = []
    for lista in matriz:
        for item in lista:
            if matriz[0][2] == setor:
                lista1.append(matriz[0][2])
    for x in range(len(lista1)):
        if lista2[x][2] == setor:
            del remove[y][2]
    return lista1