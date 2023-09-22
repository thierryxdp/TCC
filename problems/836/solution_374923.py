def busca(setor,matriz):
    '''
    
    '''
    retorno=[]
    for i in matriz:
        if i[2]==setor:
            retorno.append(i[0:2}+i[3:])
    return retorno