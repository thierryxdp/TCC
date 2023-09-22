def busca(setor,funcionarios):
    """ Essa função retorna uma lista com os funcionarios que estão presentes
    naquele setor. Como entrada temos o setor e a lista de funcionarios, e como
    saída temos uma lista desses funcionarios que se encontram neste setor;
    str,list->list"""
    lista_retorno=[]
    for i in range(len(funcionarios)):
        for j in range(len(funcionarios[1])):
            if funcionarios[i][j]==setor:
                list.append(lista_retorno,funcionarios[i])
        del lista_retorno[i][2]
    return lista_retorno