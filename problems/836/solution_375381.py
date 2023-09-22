def busca(setor,dados):
    ''' '''
    info=[]
    for i in range(len(dados)):
        if dados[i][2]==setor:
            info = info+[dados[i]]
    return list.del(info,info[i][2])