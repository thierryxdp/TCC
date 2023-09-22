def busca (setor,matriz):
    '''c'''
    resp=[]
    resp2=[]
    for i in matriz:
        for j in i:
            if setor in j:
                resp+=i
        list.pop(resp,list.index(resp,setor))
    return resp