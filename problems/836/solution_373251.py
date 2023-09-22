def busca(setor, m):
    '''
    dada uma matriz de informações, retorna, a partir do setor, informações dos funcionários
    str, list -> list
    '''
    nlin = (len(m))
    resposta=[]
    for i in range(len(m)):
        if m[i][2]==setor:
            del m[i][2]
        if m[i][2]!=setor:
            del m[i]
    return m