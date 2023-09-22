def busca(setor,matriz):
    "funcao que recebe uma matriz e faz uma busca por setor.str,list->list."
    doSetor = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == setor:
                doSetor.append(matriz[i])
    for k in range(len(doSetor)):
        del doSetor[k][2]
    return doSetor