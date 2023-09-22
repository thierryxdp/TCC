def busca(matriz,setor):
    '''Recebe uma matriz e realiza uma busca por setor, retorna os dados de todos os funcionarios deste setor;
    list,str->list'''
    
    informacoes = []
    
    for i in matriz:
        if matriz[2] == setor:
            list.append(informacoes,(i[0:2]+i[3:]))
    return informacoes