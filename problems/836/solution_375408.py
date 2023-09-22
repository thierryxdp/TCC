def busca (setor,matriz):
    """dado o nome de um setor da empresa, a função retorna uma lista com os dados de todos os funcionários daquele setor; str,list->list"""
    funcionarios=[]
    adicionar=()
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][2]==setor:
                adicionar=matriz[i]-matriz[i][2]
                funcionarios=list.append(funcionarios,adicionar)
    return funcionarios