def busca(setor,dados):
    ''' '''
    info=[]
    for i in range(len(dados)):
        if dados[i][2]==setor:
            info = info+dados[i]-dados[i][2]
    return info