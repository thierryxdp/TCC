def busca(matriz,setor):
    '''Recebe uma matriz e realiza uma busca por setor, retorna os dados de todos os funcionarios deste setor;
    list,str->list'''
    
    lista = []
    
    for i in matriz:
        if i[2] == setor:
            list.append(lista,(i[0:2]+i[3:]))
    return lista