def busca(setor,matriz):
    '''string,list --> list'''
   
    info=[]
   
    for linha in matriz:
        if setor in linha:
            info=info+[linha[0:2]+[linha[3]]]


    return info