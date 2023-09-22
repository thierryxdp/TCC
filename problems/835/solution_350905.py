def melhor_volta(M):
    corredor=0
    corredor2=0
    melhores=[]
    for i in M:
        melhor=min(M[corredor])
        list.append(melhores,melhor)
        corredor+=1
    
    melhor_v=min([melhores])
    for i in M:
        if melhor_v in M[corredor2]:
            q=corredor+1
            volta=list.index(M[corredor2],melhor_v)+1
    return (q,melhor_v,volta)