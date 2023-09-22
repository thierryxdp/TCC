def busca(m,setor):
    '''
    dada uma matriz de informações, retorna, a partir do setor, informações dos funcionários
    list, str -> tuple
    '''
    nlin = len(m)
    resposta=[]
    for i in range(nlin):
        if m[i][2]==setor:
            m.pop(m[i][2])
            resposta = list.append(resposta,m[i])
        else:
            resposta = []
    return resposta