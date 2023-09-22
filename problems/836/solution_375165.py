def busca(setor,matriz):
    '''string,list --> list'''
   
    info=[]
   
    for linha in matriz:
        if setor in linha:
            info=info+[linha]

    for pessoa in range(len(info)):
        list.remove(info[pessoa],setor)

    return info