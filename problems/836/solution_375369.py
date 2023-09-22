def busca(setor,dados):
    ''' '''
    info=[]
    for i in range(len(dados)):
        for j in range(len(dados[i])):
            if dados[i][j]==setor:
                info = info+[dados[i]]
        return info