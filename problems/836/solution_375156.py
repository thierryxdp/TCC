def busca(setor,matriz):
    '''string,list --> list'''
    
    info=[]
    
    for pessoa in matriz:
    	if setor in pessoa:
            list.append(info,pessoa)
            list.remove(info,setor)
    
    return info