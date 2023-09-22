def busca(m, setor):
    '''
    dada uma matriz de informações, retorna, a partir do setor, informações dos funcionários
    list, str -> tuple
    '''
    nlin = len(m)
    resposta=[]
    for i in range(nlin):
        ncol = len(m[i])
        for el in range(ncol):
            if m[i][el] == setor:
                resposta = [[m[i][0]],[[m[i][1]],[m[i][3]]]
                            else:
                            resposta = []
    return resposta