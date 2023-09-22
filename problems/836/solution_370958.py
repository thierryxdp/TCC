def busca(setor,matriz):
    '''dada uma matriz e um setor, retorna todos os 
    funcionários daquele setor;list,str -> list'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    listafinal = []
    i = 0
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == setor:
                listafinal.append(matriz[i])
                i += 1
            else:
                listafinal
                i += 1
    return listafinal