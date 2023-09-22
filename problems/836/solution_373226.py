def busca(setor, m):
    '''
    dada uma matriz de informações, retorna, a partir do setor, informações dos funcionários
    list, str -> tuple
    '''
    nlin = len(m)
    resposta=[]
    for i in range(nlin):
        if m[i][2]==setor:
            m.pop([i][2])
            resposta = resposta.append(resposta,m[i])
        else:
            resposta = []
    return resposta