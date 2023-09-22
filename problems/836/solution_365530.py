def busca(setor,matriz):
    '''funcao que dado o nome de um setor da empresa, retorna os dados de todos os funcionarios daquele setor
    matriz->lista'''
    listaresultados=[]
    for i in range(len(matriz)):
                   for j in range(len(matriz[i])):
                        if matriz[i][2]==setor:
                    list.append(listaresultados,matriz[i])
    return listaresultados