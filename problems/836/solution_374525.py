def busca (setor,matriz):
    '''c'''
    resp=[]
    resp2=[]
    for i in matriz:
        for j in i:
            if setor in j:
                resp+=i
                resp2+=([[resp[0],resp[1],resp[3],resp[0][1]]])
    return resp2