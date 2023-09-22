def busca(setor, matriz):
    '''
    Função que receba de entrada o nome de um setor
    de uma empresa e uma matriz que armazena informações
    e retorne os dados de todos os funcionarios daquele 
    setor
    str,list->list
    '''
    lista_retorno = []
    for i in matriz:
        if i[2] == setor:
            lista_retorno.append(i[0:2] + i[3:])
    return lista_retorno