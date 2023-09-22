def busca(setor: str, P:list)->list:
    '''Retorna dados de um funcionário de um setor especifico'''
    lista_retorno=[]
    for i in P:
        if i[2] == setor:
            lista_retorno.append(i[0:2]+i[3:])
    return lista_retorno