def busca(matriz,setor):
    '''Recebe uma matriz e realiza uma busca por setor, retorna os dados de todos os funcionarios deste setor;
    list,str->list'''
    
    informacoes=[]
    
    for i in matriz:
        if i[2] == setor:
            informacoes.append(i[:2] + i[3:])
    return informacoes