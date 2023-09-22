def busca (setor,matriz):
    """dado o nome de um setor da empresa, a função retorna uma lista com os dados de todos os funcionários daquele setor; str,list->list"""
    funcionarios=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][2]==setor:
                funcionarios+=list(matriz[i][0]+matriz[i][1]+matriz[i][3])
    return funcionarios