def busca(setor,matriz):
    '''função que retorna os dados de todos os funcionários de um setor.
    	string,lista->lista'''
    result=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            result=result+[[matriz[i][0],matriz[i][1],matriz[i][2],matriz[i][3]]]
    return result