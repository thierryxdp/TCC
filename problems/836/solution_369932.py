def busca(setor, matriz):
    """dado uma matriz e
    um setor, a funcao procura os funcionarios daquele setor
    list,str->list"""
    procura = []
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if matriz[l][c] == setor:
                list.append(procura,matriz[l][0:c]+matriz[l][c+1:])
    return procura