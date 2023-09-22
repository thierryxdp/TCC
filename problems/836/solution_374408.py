def busca (setor,matriz):
    '''c'''
    resp=[]
    for i in matriz:
        for j in i:
            if setor in j:
                list.append(resp,i)
                resp=str(resp)
                resp=str.strip(resp,setor)
                
    return list(resp)