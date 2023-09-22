def busca(m,setor):
    '''
    dada uma matriz de informações, retorna, a partir do setor, informações dos funcionários
    list, str -> tuple
    '''
    nlin = len(m)
    resposta=[]
    for i in range(nlin):
            if m[i][2] == setor:
                m.pop[[i][2]]
                resposta = resposta.append(resposta,matriz[i])
            elif m[i][2] != setor:
                resposta = []
    return resposta