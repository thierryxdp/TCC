def busca(setor,matriz):
    """Dado um nome de um setor da empresa, a funcao retorna os dados de
    todos os funcionarios daquele setor; str,list(list) -> list(list)"""

    nlin = len(matriz)
    ncol = len(matriz[0])
    registros = []
    indice = 0

    for i in range(nlin):
        if setor in matriz[i]:
            registros = registros + [matriz[i]]
            del matriz[indice][2]
        indice = indice + 1
    return registros