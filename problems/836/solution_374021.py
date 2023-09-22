def busca(setor,matriz):
    """A função retorna dados de todos os funcionários de um determinado
    setor.
    str-->list"""
    lista1 = []
    for lista in matriz:
        for item in lista:
            if matriz[lista][item] == setor:
                lista1.append(matriz[lista][item])
    if len(lista1) == 0:
        return []
    return lista1