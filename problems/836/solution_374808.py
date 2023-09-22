def busca(setor,matriz):
    """Função que faz uma busca pelo setor e retorna os dados
    de todos os funcionários daquele setor.
    str, list->list."""
    doSetor = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == setor:
                doSetor.append(matriz[i])
    for k in range(len(doSetor)):
        del doSetor[k][2]
    return doSetor