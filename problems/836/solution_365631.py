def busca(setor,matriz):
    '''Dada uma matriz de dados de funcionários e o nome de um setor da empresa, retorna todos os funcionários do setor'''
    '''str,list->list'''
    resultado=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            resultado+=[[matriz[i][0],matriz[i][1],matriz[i][3]]]
    return resultado