def busca (setor,matriz):
    '''c'''
    resp=[]
    for i in matriz:
        for j in i:
            if setor in j:
                resp+=i
                resp=list.pop(resp,2)
    return resp