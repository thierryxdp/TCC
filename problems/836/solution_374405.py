def busca (setor,matriz):
    '''c'''
    resp=[]
    for i in matriz:
        for j in i:
            if setor in j:
                list.append(resp,i)
    return [[resp[0][0],resp[0][1],resp[0][3]]]