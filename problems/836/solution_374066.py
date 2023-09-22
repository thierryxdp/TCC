def busca(setor,matriz):
    '''Essa funcao analisa uma matriz de entrada que possui 4 
    colunas, onde na coluna 3 esta os setor dos funcionarios de
    uma empresa. a funcao recebe um setor especifico e retorna todos os dados
    de todos os funcionários desse setor
    str,list->list'''
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==setor:
                lista+=[[matriz[i][0]]+[matriz[i][1]]+[matriz[i][3]]]              
    return lista