def busca (setor,matriz):
    '''c'''
    resp=[]
    for i in matriz:
        for j in i:
            if setor in j:
                list.append(resp,i)
                list.remove(resp,list.index(resp,resp[j]))
    return resp