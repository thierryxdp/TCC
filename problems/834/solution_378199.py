def media_matriz(matriz:list)->float:
    numero_linhas = len(matriz)
    numero_colunas = len(matriz[0])
    num_inteiros = numero_linhas*numero_colunas
    return round(sum(map(sum, matriz))/num_inteiros,2)