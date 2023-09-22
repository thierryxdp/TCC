def busca(setor:str,P:list)->list:
    '''dado o setor retorna os nomes dos funcionários e os respectivos dados da lista'''
    retorno=[]
    for i in P:
        if i[2] == setor:
            retorno.append(i[0:2]+i[3:])
    return retorno