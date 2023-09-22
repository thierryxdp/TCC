def busca (setor,matriz):
    """dado o nome de um setor da empresa, a função retorna uma lista com os dados de todos os funcionários daquele setor; str,list->list"""
    funcionarios=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            del (matriz[i])[2]
            funcionarios=list.append(funcionarios,matriz[i])
    return funcionarios