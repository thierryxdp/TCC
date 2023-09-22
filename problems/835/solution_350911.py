def melhor_volta(M):
    corredor=0
    corredor2=0
    melhores=[]
    for i in M:
        melhor=min(M[corredor])
        list.append(melhores,melhor)
        melhor_v=min([melhores])
        if melhor_v in M[corredor]:
            q=corredor+1
            volta=list.index(M[corredor],melhor_v)+1
        corredor+=1
    return (q,melhor_v,volta)