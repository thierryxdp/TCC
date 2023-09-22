def busca (setor,matriz):
    """dado o nome de um setor da empresa, a função retorna uma lista com os dados de todos os funcionários daquele setor; str,list->list"""
    funcionarios=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][2]==setor:
                funcionarios=list.append(funcionarios,matriz[i]-matriz[i][2])
    return funcionarios