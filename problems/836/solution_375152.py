def busca(setor,matriz):
    '''string,list --> list'''
    
    info=[]
    
    for linha in matriz:
        if setor in linha:
            info=info+[linha]
            info=list.remove(info,setor)
    
        
    return info