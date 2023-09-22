def busca(m, setor):
    '''
    dada uma matriz de informações, retorna, a partir do setor, informações dos funcionários
    list, str -> tuple
    '''
    nlin = len(m)
    ncol = len(m[i])
    resposta=[]
    for i in range(nlin):
        for el in range(ncol):
            if m[i][2] == setor:
                resposta = [m[i][0],[mi][1],m[i][3]]
            else:
                resposta = []
    return resposta