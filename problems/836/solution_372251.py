def busca(setor,matriz):
    '''Função que retorna as informações dos funcionários
    de um setor; recebe como parâmetro um setor de trabalho
    da empresa e a matriz com todos os funcionários e suas
    informações; string,list(list)-->list(list)'''
    linha=len(matriz)
    coluna=len(matriz[0])
    mat_inf=[]
    for i in range(len(matriz)):
    	if setor==matriz[i][2]:
            del matriz[i][2]
            list.append(mat_inf,[matriz[i]])
    return mat_inf