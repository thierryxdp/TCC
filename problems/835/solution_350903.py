def melhor_volta(M):
    corredor=0
    melhores=[]
    for i in M:
        melhor=min(M[corredor])
        list.append(melhores,melhor)
        corredor+=1
    
    melhor_v=min([melhores])
    for i in M:
        if melhor_v in M[corredor]:
            quem=corredor+1
            volta=list.index(M[corredor],melhor_v)+1
    return (quem,melhor_v,volta)