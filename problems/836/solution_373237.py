def busca(setor, m):
    '''
    dada uma matriz de informações, retorna, a partir do setor, informações dos funcionários
    str, list -> list
    '''
    nlin = len(m)
    resposta=[]
    for i in range(nlin):
        if m[i][2]==setor:
            del(m[i][2])
            resposta = resposta + list.append(resposta,m[i])
        else:
            resposta = []
    return resposta