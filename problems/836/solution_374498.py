def busca (setor,matriz):
    '''c'''
    resp=[]
    resp2=[]
    indice=2
    for i in matriz:
        for j in i:
            if setor in j:
                list.append(resp,i)
                del resp [indice]
                list.append(resp2,([resp[0][0],resp[0][1],resp[0][3]]))
        indice+=2
    return resp