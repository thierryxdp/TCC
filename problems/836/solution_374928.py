def busca(setor,matriz):
    '''
    
    '''
    ret=[]
    for i in matriz:
        if (i[2])==setor:
            ret.append(i[0:2]+i[3:])
    return ret