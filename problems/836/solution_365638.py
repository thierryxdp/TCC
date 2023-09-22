def busca(matriz,setor):
    '''busca recebe uma matriz com 4 colunas e um setor e devolve os dados de todos os funcionarios deste setor.
    Assume uma matriz com 4 colunas.
    list,str-->list'''
    dados=[]
    for i in range(len(matriz)):
        if setor in matriz[i][2]:
            dados=dados+[[matriz[i][0],matriz[i][1],matriz[i][3]]]
    return dados