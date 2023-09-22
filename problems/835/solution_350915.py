def melhor_volta(M):
    corredor=0
    voltas=0
    melhores=[]
    for i in M:
        melhor=min(M[corredor])
        list.append(melhores,melhor)
        melhor_v=min(melhores)
        for j in M[corredor]:
            if j==melhor_v:
                quem=corredor+1
                volta=list.index(M[corredor],j)+1
        corredor+=1
    return (quem,melhor_v,volta)