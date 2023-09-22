def busca(setor: str, P:list)->list:
    '''recebe uma matriz e um setor e retorna 
    os dados dos funcionários daaquele setor'''
    lista_retorno=[]
    for i in P:
        if i[2] == setor:
            lista_retorno.append(i[0:2]+i[3:])
    return lista_retorno