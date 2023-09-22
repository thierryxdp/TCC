def busca (setor,matriz):
    '''c'''
    resp=[]
    resp2=[]
    for i in matriz:
        for j in i:
            if setor in j:
                list.append(resp,(i[0],i[1],i[3]))
    return resp