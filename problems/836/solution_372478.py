def busca(setor,P):
    '''Esta e a funcao que'''
    lista1=[]
    i=0
    for item in P[i][2]:
        if item==setor:
            lista1.append(P[i][:1])
            lista1.append(P[i][3])
        i+=1    
    return lista1