def busca(setor,dados):
    ''' '''
    info=[]
    for i in range(len(dados)):
        if dados[i][2]==setor:
            info = [info+[dados[i][0]]+[dados[i][1]]+[dados[i][3]]]
    return info