def busca (setor,matriz):
    '''c'''
    resp=[]
    resp2=[]
    for i in matriz:
        for j in i:
            if setor in j:
                list.append(resp,([i[0][0],i[0][1],i[0][3]]))
    return resp2