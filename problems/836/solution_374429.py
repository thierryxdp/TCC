def busca (setor,matriz):
    '''c'''
    resp=[]
    for i in matriz:
        for j in i:
            if setor in j:
                list.append(resp,i)
        del resp[2]
    return resp