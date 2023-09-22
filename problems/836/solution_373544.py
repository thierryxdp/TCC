def busca(setor: str, P:list)->list:
    '''Retorna dados de um funcionário de determinado setor'''
    for i in P:
        if i in [2] == setor:
            lista_retorno.append(i[0:2]+I[3:])
    return lista_retorno