def busca (setor,matriz):
    '''c'''
    resp=[]
    resp2=[]
    for i in matriz:
        for j in i:
            if setor in j:
                list.append(resp,i)
                list.append(resp2,([resp[0][0],resp[0][1],resp[0][3],resp[1][0],resp[1][1],resp[1][2]]))
    return resp2