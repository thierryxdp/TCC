def busca(matriz,setor):
    '''funcao que dado o nome de um setor da empresa, retorna os dados de todos os funcionarios daquele setor
    matriz->lista'''
    listaresultado=[]
    for i in range(len(matriz)):
                   for j in range(len(matriz[i])):
                		if matriz[i][2]==setor:
                        return matriz[i]