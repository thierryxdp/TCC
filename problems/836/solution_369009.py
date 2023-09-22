def busca(setor,matriz):
    '''dado um setor e uma matriz contendo informaçoes dos 
    funcionarios retorna quais funcionarios pertemcem ao setor
    desejado
    str,list->list'''
	funcionarios=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            del matriz[i][2]
            funcionarios+=[matriz[i]]
    return funcionarios